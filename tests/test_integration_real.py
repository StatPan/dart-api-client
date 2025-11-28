"""
Integration test for dart-api-client with real DART API.
Only runs if DART_API_KEY is set in environment.
"""
import asyncio
import os
import sys
from pathlib import Path

# Add parent .env support
env_file = Path(__file__).parent.parent.parent / ".env"
if env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(env_file)

from dart_client import DartAPIClient

async def test_real_api():
    api_key = os.getenv("DART_API_KEY")
    if not api_key:
        print("⚠️  DART_API_KEY not set. Skipping real API tests.")
        return False
    
    print("🔍 Testing dart-api-client with real DART API...")
    print(f"   API Key: {api_key[:10]}...")
    
    async with DartAPIClient(api_key=api_key) as client:
        # Test 1: get_corp_code (ZIP/XML download)
        print("\n[1/4] Testing get_corp_code (고유번호 - ZIP/XML)...")
        try:
            corp_codes = await client.get_corp_code()
            print(f"  ✅ Downloaded {len(corp_codes)} corporation codes")
            print(f"  Sample: {corp_codes[0].corp_name} ({corp_codes[0].corp_code})")
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        # Test 2: get_company (기업개황)
        print("\n[2/4] Testing get_company (기업개황)...")
        try:
            # Use Samsung Electronics
            company = await client.get_company(corp_code="00126380")
            print(f"  ✅ Got company info")
            print(f"  Status: {company.get('status')}")
            if company.get('status') == '000':
                print(f"  Company: {company.get('corp_name', 'N/A')}")
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        # Test 3: get_list (공시검색)
        print("\n[3/4] Testing get_list (공시검색)...")
        try:
            result = await client.get_list(
                corp_code="00126380",
                bgn_de="20240101",
                end_de="20240131",
                page_count=5
            )
            print(f"  ✅ Got disclosure list")
            print(f"  Status: {result.get('status')}, Message: {result.get('message')}")
            if 'total_count' in result:
                print(f"  Total count: {result.get('total_count')}")
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        # Test 4: get_fnltt_singl_acnt (재무제표)
        print("\n[4/4] Testing get_fnltt_singl_acnt (단일회사 주요계정)...")
        try:
            financials = await client.get_fnltt_singl_acnt(
                corp_code="00126380",
                bsns_year="2023",
                reprt_code="11011"  # 사업보고서
            )
            print(f"  ✅ Got financial data")
            print(f"  Status: {financials.get('status')}, Message: {financials.get('message')}")
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    print("\n✅ All real API tests passed!")
    return True

if __name__ == "__main__":
    result = asyncio.run(test_real_api())
    sys.exit(0 if result else 1)
