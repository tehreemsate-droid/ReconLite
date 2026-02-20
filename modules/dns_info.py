import socket

def get_dns_info(host: str) -> dict:
    result = {
        "host": host,
        "ips": [],
        "error": None
    }

    try:
        info = socket.getaddrinfo(host, None)
        ips = list({item[4][0] for item in info})
        result["ips"] = ips
    except Exception as e:
        result["error"] = str(e)

    return result
