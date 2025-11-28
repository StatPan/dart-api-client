"""
Debug script to see what corpCode.xml actually returns
"""
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

env_file = Path(__file__).parent.parent.parent / ".env"
if env_file.exists():
    load_dotenv(env_file)

from dart_client import DartAPIClient

async def debug_corp_code():
    api_key = os.getenv("DART_API_KEY")
    print(f"API Key: {api_key[:10]}...")
    
    client = DartAPIClient(api_key=api_key)
    
    # Call the raw request method
    print("\nCalling api/corpCode.xml...")
    try:
        content = await client.request("api/corpCode.xml", {})
        print(f"Response type: {type(content)}")
        print(f"Response length: {len(content) if isinstance(content, (bytes, str)) else 'N/A'}")
        
        if isinstance(content, dict):
            print(f"JSON Response: {content}")
        elif isinstance(content, bytes):
            print(f"First 200 bytes: {content[:200]}")
            # Check if it's really a ZIP
            print(f"Starts with ZIP magic: {content[:4] == b'PK\\x03\\x04'}")
        else:
            print(f"Content: {content[:200]}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(debug_corp_code())
