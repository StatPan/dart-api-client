import asyncio
import io
import zipfile
from unittest.mock import MagicMock, patch
from dart_client import DartAPIClient
from dart_client.models.corp_code import CorpCode
from dart_client.models.disclosure import DisclosureList

async def test_manual():
    print("Starting manual test...")
    
    # Mock data for CorpCode
    mock_xml = b"""
    <result>
        <list>
            <corp_code>00126380</corp_code>
            <corp_name>Samsung Electronics</corp_name>
            <stock_code>005930</stock_code>
            <modify_date>20240101</modify_date>
        </list>
    </result>
    """
    
    # Create a valid ZIP file in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('CORPCODE.xml', mock_xml)
    zip_content = zip_buffer.getvalue()

    # Mock data for Disclosure
    mock_json = {
        "status": "000",
        "message": "Normal",
        "page_no": 1,
        "page_count": 10,
        "total_count": 1,
        "total_page": 1,
        "list": [
            {
                "corp_code": "00126380",
                "corp_name": "Samsung Electronics",
                "stock_code": "005930",
                "corp_cls": "Y",
                "report_nm": "Quarterly Report",
                "rcept_no": "20240101000001",
                "flr_nm": "Samsung",
                "rcept_dt": "20240101",
                "rm": ""
            }
        ]
    }

    # Mocking the client.request method to avoid real network calls
    with patch('dart_client.client.DartAPIClient.request') as mock_request:
        client = DartAPIClient(api_key="dummy")
        
        # Test 1: Get Corp Code
        print("\nTest 1: get_corp_code")
        mock_request.return_value = zip_content
        corp_codes = await client.get_corp_code()
        print(f"Result: {corp_codes}")
        assert len(corp_codes) == 1
        assert isinstance(corp_codes[0], CorpCode)
        assert corp_codes[0].corp_name == "Samsung Electronics"
        print("PASS")

        # Test 2: Search Disclosure
        print("\nTest 2: search_disclosure")
        mock_request.return_value = mock_json
        disclosures = await client.search_disclosure(corp_code="00126380")
        print(f"Result: {disclosures}")
        assert isinstance(disclosures, DisclosureList)
        assert len(disclosures.list) == 1
        assert disclosures.list[0].report_nm == "Quarterly Report"
        print("PASS")

if __name__ == "__main__":
    asyncio.run(test_manual())
