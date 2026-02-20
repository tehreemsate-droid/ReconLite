import requests

def check_common_files(base_url: str, timeout: int = 8) -> dict:
    paths = ["robots.txt", "sitemap.xml"]
    results = {}

    # If site redirects to http (like your http_info shows), try http first
    candidates = [base_url]
    if base_url.startswith("https://"):
        candidates = ["http://" + base_url[len("https://"):], base_url]

    for path in paths:
        last_error = None
        for b in candidates:
            url = f"{b}/{path}"
            try:
                r = requests.get(url, timeout=timeout, allow_redirects=True)
                results[path] = {
                    "requested_url": url,
                    "final_url": r.url,
                    "status_code": r.status_code,
                    "found": r.status_code == 200
                }
                last_error = None
                break
            except Exception as e:
                last_error = str(e)

        if last_error is not None and path not in results:
            results[path] = {
                "error": last_error,
                "found": False
            }

    return results
