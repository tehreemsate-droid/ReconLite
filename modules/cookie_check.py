def check_cookies(headers: dict) -> dict:
    results = []

    if not headers:
        return {"cookies": [], "note": "No headers available"}

    set_cookie = headers.get("Set-Cookie") or headers.get("set-cookie")

    if not set_cookie:
        return {"cookies": [], "note": "No cookies set"}

    cookies = set_cookie.split(",")

    for cookie in cookies:
        cookie_info = {
            "raw": cookie.strip(),
            "HttpOnly": "httponly" in cookie.lower(),
            "Secure": "secure" in cookie.lower(),
            "SameSite": "samesite" in cookie.lower(),
        }
        results.append(cookie_info)

    return {"cookies": results}
