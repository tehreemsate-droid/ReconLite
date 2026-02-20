import requests

def get_http_info(base_url: str, timeout: int = 8) -> dict:
    result = {
        "base_url": base_url,
        "final_url": None,
        "status_code": None,
        "headers": {},
        "https": base_url.startswith("https://"),
        "tried_http_fallback": False,
        "error": None
    }

    def _try(url: str):
        r = requests.get(url, timeout=timeout, allow_redirects=True)
        return r

    try:
        response = _try(base_url)
        result["final_url"] = response.url
        result["status_code"] = response.status_code
        result["headers"] = dict(response.headers)
        result["https"] = response.url.startswith("https://")
        return result

    except Exception as e_https:
        # Agar https fail ho gaya aur url https hai, to http try karo
        if base_url.startswith("https://"):
            try:
                http_url = "http://" + base_url[len("https://"):]
                result["tried_http_fallback"] = True
                response = _try(http_url)

                result["final_url"] = response.url
                result["status_code"] = response.status_code
                result["headers"] = dict(response.headers)
                result["https"] = response.url.startswith("https://")
                result["error"] = None
                return result

            except Exception as e_http:
                result["error"] = f"HTTPS failed: {e_https} | HTTP failed: {e_http}"
                return result

        result["error"] = str(e_https)
        return result

