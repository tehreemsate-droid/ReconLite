def check_security_headers(headers: dict) -> dict:
    headers_lower = {k.lower(): v for k, v in (headers or {}).items()}

    important_headers = [
        "content-security-policy",
        "strict-transport-security",
        "x-content-type-options",
        "x-frame-options",
        "referrer-policy",
        "permissions-policy",
    ]

    missing = []
    present = {}

    for header in important_headers:
        if header in headers_lower:
            present[header] = headers_lower[header]
        else:
            missing.append(header)

    return {
        "missing_headers": missing,
        "present_headers": present
    }
