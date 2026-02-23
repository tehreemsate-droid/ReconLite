import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

# Modules
from modules.dns_info import get_dns_info
from modules.http_info import get_http_info
from modules.security_headers import check_security_headers
from modules.robots_check import check_common_files
from modules.cookie_check import check_cookies

# Utils
from utils.common import normalize_target
from utils.print_report import print_summary


VERSION = "1.0.0"


def main():
    # Ensure output directory exists
    BASE_DIR = Path(__file__).resolve().parent
    OUTPUT_DIR = BASE_DIR / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description="ReconLite - Modular Recon + Safe Vulnerability Checks"
    )

    parser.add_argument("target", help="Domain or URL (e.g., example.com)")
    parser.add_argument("--timeout", type=int, default=8, help="Request timeout (seconds)")
    parser.add_argument("--version", action="store_true", help="Show version and exit")

    args = parser.parse_args()

    if args.version:
        print(f"ReconLite v{VERSION}")
        return

    target = normalize_target(args.target)

    timestamp = int(datetime.now(timezone.utc).timestamp())

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

    # Run modules
    results["dns"] = get_dns_info(target["host"])
    results["http"] = get_http_info(target["base_url"], timeout=args.timeout)
    results["security_headers"] = check_security_headers(
        results["http"].get("headers", {})
    )
    results["cookies"] = check_cookies(
        results["http"].get("headers", {})
    )
    results["common_files"] = check_common_files(
        target["base_url"], timeout=args.timeout
    )

    # Print summary
    print_summary(results)

    # Save output
    out_name = OUTPUT_DIR / f"{target['host']}_{timestamp}.json"

    with open(out_name, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\n[+] Done. Saved: {out_name.resolve()}")


if __name__ == "__main__":
    main()