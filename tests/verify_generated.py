import asyncio
from dart_client import DartAPIClient

async def verify_generated_methods():
    """Verify that the client properly exposes all generated methods."""
    
    print("Verifying dart-api-client with generated methods...")
    
    client = DartAPIClient(api_key="test_key")
    
    # Check that methods exist
    expected_methods = [
        "get_list",
        "get_company",
        "get_corp_code",
        "get_irds_sttus",
        "get_fnltt_singl_acnt",
        "get_majorstock",
        "get_piic_decsn",
        "get_estk_rs"
    ]
    
    for method in expected_methods:
        if not hasattr(client, method):
            print(f"❌ Missing method: {method}")
            return False
        print(f"✓ Found method: {method}")
    
    # Count all get_ methods
    all_methods = [m for m in dir(client) if m.startswith("get_")]
    print(f"\n✓ Total 'get_*' methods: {len(all_methods)}")
    print(f"  Expected: 83 + 2 custom (get_corp_code, search_disclosure)")
    
    # Verify inheritance
    from dart_client.generated import GeneratedDartAPIMixin
    if isinstance(client, GeneratedDartAPIMixin):
        print("✓ Client correctly inherits from GeneratedDartAPIMixin")
    else:
        print("❌ Client missing GeneratedDartAPIMixin inheritance")
        return False
    
    # Verify async signature
    import inspect
    if inspect.iscoroutinefunction(client.get_company):
        print("✓ Generated methods are async")
    else:
        print("❌ Generated methods are not async")
        return False
    
    await client.close()
    print("\n✅ All checks passed!")
    return True

if __name__ == "__main__":
    asyncio.run(verify_generated_methods())
