import argparse
import json
from datetime import datetime, timezone
from modules.dns_info import get_dns_info
from modules.http_info import get_http_info
from modules.security_headers import check_security_headers
from utils.common import normalize_target, safe_filename
from utils.print_report import print_summary
from modules.robots_check import check_common_files
from modules.cookie_check import check_cookies

def main():
    parser = argparse.ArgumentParser(description="Modular Recon + Safe Vulnerability Checks")
    parser.add_argument("target", help="Domain or URL (e.g., example.com or https://example.com)")
    parser.add_argument("--timeout", type=int, default=8, help="Request timeout (seconds)")
    args = parser.parse_args()

    target = normalize_target(args.target)

    results = {
        "target_input": args.target,
        "target_normalized": target,
        "scan_time_utc": datetime.now(timezone.utc).isoformat(),
        "dns": {},
        "http": {},
        "security_headers": {},
        "common_files": {},
        "cookies": {}

    }
    
    results["dns"] = get_dns_info(target["host"])
    results["http"] = get_http_info(target["base_url"], timeout=args.timeout)
    results["security_headers"] = check_security_headers(results["http"].get("headers", {}))
    results["cookies"] = check_cookies(
    results["http"].get("headers", {})
)

    results["common_files"] = check_common_files(target["base_url"], timeout=args.timeout)

    print_summary(results)
    
    out_name = f"output/{safe_filename(target['host'])}_{int(datetime.now(timezone.utc).timestamp())}.json"
    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"[+] Done. Saved: {out_name}")


if __name__ == "__main__":
    main()
