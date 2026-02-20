def print_summary(results: dict) -> None:
    target = results.get("target_normalized", {})
    dns = results.get("dns", {})
    http = results.get("http", {})
    sec = results.get("security_headers", {})
    common = results.get("common_files", {})
    cookies_data = results.get("cookies", {})
    cookies = cookies_data.get("cookies", [])

    print("\n" + "=" * 50)
    print("RECON + SAFE VULN SUMMARY")
    print("=" * 50)

    print(f"Target   : {target.get('host')}")
    print(f"Base URL : {target.get('base_url')}")
    print(f"Scan UTC : {results.get('scan_time_utc')}")

    print("\n--- DNS ---")
    if dns.get("error"):
        print(f"DNS Error: {dns['error']}")
    else:
        ips = dns.get("ips", [])
        print(f"IPs      : {', '.join(ips) if ips else 'None'}")

    print("\n--- HTTP ---")
    if http.get("error"):
        print(f"HTTP Error: {http['error']}")
    else:
        print(f"Status    : {http.get('status_code')}")
        print(f"Final URL : {http.get('final_url')}")
        print(f"HTTPS     : {'Yes' if http.get('https') else 'No'}")

        headers = http.get("headers", {}) or {}
        server = headers.get("Server") or headers.get("server")
        powered = headers.get("X-Powered-By") or headers.get("x-powered-by")

        if server:
            print(f"Server    : {server}")
        if powered:
            print(f"X-Powered-By: {powered}")

    print("\n--- Security Headers (Safe checks) ---")
    missing = sec.get("missing_headers", [])
    if missing:
        print("Missing:")
        for h in missing:
            print(f" - {h}")
    else:
        print("Missing: None ✅")

    print("\n--- Common Files ---")
    for file, info in common.items():
        if info.get("found"):
            print(f"{file} : FOUND ✅ (Status {info.get('status_code')})")
        else:
            print(f"{file} : Not Found ❌")

    print("\n--- Cookies ---")
    if not cookies:
        print("No cookies found")
    else:
        for c in cookies:
            print("Cookie:", c.get("raw"))
            print("  HttpOnly:", c.get("HttpOnly"))
            print("  Secure:", c.get("Secure"))
            print("  SameSite:", c.get("SameSite"))

    print("=" * 50 + "\n")
