"""
Capture real DART API responses and save as fixtures for testing.
"""
import asyncio
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_file = Path(__file__).parent.parent.parent / ".env"
if env_file.exists():
    load_dotenv(env_file)

from dart_client import DartAPIClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"

async def capture_fixtures():
    api_key = os.getenv("DART_API_KEY")
    if not api_key:
        print("⚠️  DART_API_KEY not set")
        return
    
    FIXTURES_DIR.mkdir(exist_ok=True)
    print(f"📦 Capturing DART API responses to {FIXTURES_DIR}")
    
    async with DartAPIClient(api_key=api_key) as client:
        # 1. Corp Code (first 100 only to keep fixture size reasonable)
        print("\n[1/5] Capturing corp_code...")
        corp_codes = await client.get_corp_code()
        fixture_data = [code.model_dump() for code in corp_codes[:100]]
        with open(FIXTURES_DIR / "corp_code.json", "w", encoding="utf-8") as f:
            json.dump(fixture_data, f, ensure_ascii=False, indent=2)
        print(f"  ✅ Saved {len(fixture_data)} corp codes")
        
        # 2. Company (Samsung Electronics)
        print("\n[2/5] Capturing company...")
        company = await client.get_company(corp_code="00126380")
        with open(FIXTURES_DIR / "company.json", "w", encoding="utf-8") as f:
            json.dump(company, f, ensure_ascii=False, indent=2)
        print(f"  ✅ Saved company info")
        
        # 3. Disclosure List
        print("\n[3/5] Capturing disclosure list...")
        disclosures = await client.get_list(
            corp_code="00126380",
            bgn_de="20240101",
            end_de="20240131",
            page_count=10
        )
        with open(FIXTURES_DIR / "disclosure_list.json", "w", encoding="utf-8") as f:
            json.dump(disclosures, f, ensure_ascii=False, indent=2)
        print(f"  ✅ Saved disclosure list")
        
        # 4. Financial Statement
        print("\n[4/5] Capturing financial statement...")
        financials = await client.get_fnltt_singl_acnt(
            corp_code="00126380",
            bsns_year="2023",
            reprt_code="11011"
        )
        with open(FIXTURES_DIR / "financials.json", "w", encoding="utf-8") as f:
            json.dump(financials, f, ensure_ascii=False, indent=2)
        print(f"  ✅ Saved financial data")
        
        # 5. Stock ownership
        print("\n[5/5] Capturing stock ownership...")
        try:
            ownership = await client.get_hyslr_sttus(
                corp_code="00126380",
                bsns_year="2023",
                reprt_code="11011"
            )
            with open(FIXTURES_DIR / "ownership.json", "w", encoding="utf-8") as f:
                json.dump(ownership, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Saved ownership data")
        except Exception as e:
            print(f"  ⚠️  Skipped: {e}")
    
    print(f"\n✅ Fixtures saved to {FIXTURES_DIR}")

if __name__ == "__main__":
    asyncio.run(capture_fixtures())
