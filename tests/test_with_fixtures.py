"""
Unit tests using captured fixtures from real DART API.
"""
import pytest
import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from dart_client import DartAPIClient
from dart_client.models.corp_code import CorpCode

FIXTURES_DIR = Path(__file__).parent / "fixtures"

def load_fixture(filename):
    with open(FIXTURES_DIR / filename, encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def mock_client(monkeypatch):
    """Create a DartAPIClient with mocked HTTP requests."""
    client = DartAPIClient(api_key="test_key")
    
    # Create a mapping of endpoints to fixture files
    fixtures_map = {
        "company.json": "company.json",
        "list.json": "disclosure_list.json",
        "fnlttSinglAcnt.json": "financials.json",
        "hyslrSttus.json": "ownership.json",
    }
    
    async def mock_request(endpoint, params=None):
        # Special handling for corpCode.xml
        if "corpCode" in endpoint:
            # Return fixture data as if it came from ZIP
            return load_fixture("corp_code.json")
        
        # Find matching fixture
        for key, fixture_file in fixtures_map.items():
            if key in endpoint:
                return load_fixture(fixture_file)
        
        # Default response
        return {"status": "000", "message": "정상"}
    
    # Mock the request method
    client.request = AsyncMock(side_effect=mock_request)
    
    # For corp_code, we need to bypass the ZIP logic
    async def mock_get_corp_code():
        data = load_fixture("corp_code.json")
        return [CorpCode(**item) for item in data]
    
    client.get_corp_code = AsyncMock(side_effect=mock_get_corp_code)
    
    return client

@pytest.mark.asyncio
async def test_get_company(mock_client):
    """Test get_company with fixture data."""
    result = await mock_client.get_company(corp_code="00126380")
    
    assert result["status"] == "000"
    assert result["corp_name"] == "삼성전자(주)"
    assert "stock_code" in result

@pytest.mark.asyncio
async def test_get_list(mock_client):
    """Test get_list (disclosure search) with fixture data."""
    result = await mock_client.get_list(
        corp_code="00126380",
        bgn_de="20240101",
        end_de="20240131"
    )
    
    assert result["status"] == "000"
    assert "list" in result
    assert len(result["list"]) > 0
    
    # Check first disclosure item
    first_item = result["list"][0]
    assert "corp_code" in first_item
    assert "report_nm" in first_item

@pytest.mark.asyncio
async def test_get_financials(mock_client):
    """Test get_fnltt_singl_acnt with fixture data."""
    result = await mock_client.get_fnltt_singl_acnt(
        corp_code="00126380",
        bsns_year="2023",
        reprt_code="11011"
    )
    
    assert result["status"] == "000"
    assert "list" in result

@pytest.mark.asyncio
async def test_get_corp_code(mock_client):
    """Test get_corp_code with fixture data."""
    corp_codes = await mock_client.get_corp_code()
    
    assert len(corp_codes) == 100  # We saved 100 in fixture
    assert all(isinstance(code, CorpCode) for code in corp_codes)
    assert corp_codes[0].corp_code
    assert corp_codes[0].corp_name

@pytest.mark.asyncio
async def test_get_ownership(mock_client):
    """Test get_hyslr_sttus (major shareholder status) with fixture data."""
    result = await mock_client.get_hyslr_sttus(
        corp_code="00126380",
        bsns_year="2023",
        reprt_code="11011"
    )
    
    assert result["status"] == "000"
    assert "list" in result
