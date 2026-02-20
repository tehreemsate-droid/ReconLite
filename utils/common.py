from urllib.parse import urlparse

def normalize_target(user_input: str) -> dict:
    s = user_input.strip()

    # Agar http/https nahi likha to default https laga do
    if "://" not in s:
        s = "https://" + s

    parsed = urlparse(s)
    host = parsed.netloc or parsed.path
    host = host.strip("/")

    base_url = f"{parsed.scheme}://{host}"

    return {
        "host": host,
        "base_url": base_url
    }


def safe_filename(name: str) -> str:
    # Invalid characters ko remove karega
    return "".join(
        c if c.isalnum() or c in ("-", "_", ".") else "_"
        for c in name
    )
