import os
import httpx
import io
import zipfile
import xmltodict
from aiolimiter import AsyncLimiter
from typing import Any, Optional

from .errors import DartAPIError, DartAuthError, DartLimitError
from .models.corp_code import CorpCode
from .models.disclosure import Disclosure, DisclosureList
from .generated import GeneratedDartAPIMixin

class DartAPIClient(GeneratedDartAPIMixin):
    """
    Async client for the DART API.
    """
    BASE_URL = "https://opendart.fss.or.kr/api"

    def __init__(
        self,
        api_key: Optional[str] = None,
        requests_per_minute: int = 100,
        limiter: Optional[AsyncLimiter] = None,
    ):
        """
        Initialize DartAPIClient.
        
        Args:
            api_key: DART API Key. If None, tries to read from DART_API_KEY env var.
            requests_per_minute: Max requests per minute (default: 100).
            limiter: Optional external AsyncLimiter instance (e.g. for sharing across tasks).
                     If provided, requests_per_minute is ignored.
        """
        self.api_key = api_key or os.getenv("DART_API_KEY")
        if not self.api_key:
            raise ValueError("DART_API_KEY is required")
            
        self.client = httpx.AsyncClient(timeout=30.0)
        
        # Use provided limiter or create new one
        if limiter:
            self.limiter = limiter
        else:
            self.limiter = AsyncLimiter(max_rate=requests_per_minute, time_period=60)

    def __del__(self):
        if hasattr(self, "client") and not self.client.is_closed:
            # We cannot await here, but we can warn the user
            import warnings
            warnings.warn(
                "DartAPIClient was not closed. Use 'async with DartAPIClient(...)', or call 'await client.close()'.",
                ResourceWarning
            )

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def request(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any] | bytes:
        """
        Make a request to the DART API.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        params = params or {}
        params["crtfc_key"] = self.api_key

        async with self.limiter:
            response = await self.client.get(url, params=params)
        
        # Check HTTP status first
        response.raise_for_status()

        # DART returns JSON for most endpoints, but ZIP/XML for some
        content_type = response.headers.get("content-type", "")
        if "application/zip" in content_type or "application/octet-stream" in content_type:
             return response.content

        try:
            data = response.json()
        except Exception:
             # Fallback for non-JSON responses (e.g. XML string if not zipped)
             return response.content

        # Check DART specific error codes
        if not isinstance(data, dict):
            # Should not happen if response.json() succeeded, but safe guard
            return data

        # Check status code
        status = data.get("status")
        if status is None:
            # If JSON but no status, it might be a different API structure or error
            raise DartAPIError("INVALID_RESPONSE", "Response JSON missing 'status' field")

        message = data.get("message", "")
        
        if status != "000":
            if status == "010":
                raise DartAuthError(status, message)
            elif status == "020":
                raise DartLimitError(status, message)
            else:
                raise DartAPIError(status, message)
                
        return data

    async def get_corp_code(self) -> list[CorpCode]:
        """
        Fetch the list of unique corporation codes.
        Returns a list of CorpCode models.
        """
        # 1. Download ZIP (or error XML)
        content = await self.request("corpCode.xml")
        if not isinstance(content, bytes):
            raise DartAPIError("INVALID_RESPONSE", "Expected bytes response for corpCode.xml")

        # 2. Check if response is error XML (starts with <?xml)
        if content.startswith(b'<?xml'):
            # Parse error response
            parsed = xmltodict.parse(content)
            result = parsed.get("result", {})
            status = result.get("status")
            message = result.get("message", "Unknown error")
            
            if status == "020":
                raise DartLimitError(status, message)
            elif status and status != "000":
                raise DartAPIError(status, message)

        # 3. Extract XML from ZIP
        with zipfile.ZipFile(io.BytesIO(content)) as zf:
            xml_filename = zf.namelist()[0]  # Usually CORPCODE.xml
            xml_data = zf.read(xml_filename)

        # 4. Parse XML
        parsed = xmltodict.parse(xml_data)
        
        # 5. Extract list
        result = parsed.get("result", {})
        items = result.get("list", [])
        
        if isinstance(items, dict):
            items = [items]
            
        return [CorpCode(**item) for item in items]

    async def search_disclosure(
        self, 
        corp_code: Optional[str] = None, 
        bgn_de: Optional[str] = None, 
        end_de: Optional[str] = None, 
        pblntf_ty: Optional[str] = None, 
        last_reprt_at: Optional[str] = None,
        page_no: int = 1,
        page_count: int = 10
    ) -> DisclosureList:
        """
        Search for disclosures.
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
            "pblntf_ty": pblntf_ty,
            "last_reprt_at": last_reprt_at,
            "page_no": page_no,
            "page_count": page_count
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        
        data = await self.request("list.json", params)
        if isinstance(data, bytes):
             raise DartAPIError("INVALID_RESPONSE", "Expected JSON response for list.json")
             
        return DisclosureList(**data)
