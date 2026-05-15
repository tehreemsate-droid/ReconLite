import requests

def detect_waf(url):
    print(f"\n[*] Checking for WAF on: {url}")
    
    # Common WAF Signatures in Headers
    waf_signatures = {
        'Cloudflare': 'cf-ray',
        'Akamai': 'akamai-ch',
        'Sucuri': 'x-sucuri-id',
        'ModSecurity': 'mod_security',
        'AWS WAF': 'awselb'
    }

    try:
        # 1. Normal Request to check headers
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        for name, signature in waf_signatures.items():
            if signature in str(headers).lower():
                return f"[!] WAF Detected: {name}"

        # 2. Provoke WAF with a basic XSS payload
        payload = "?id=<script>alert(1)</script>"
        attack_url = url + payload
        attack_res = requests.get(attack_url, timeout=10)
        
        if attack_res.status_code == 403 or attack_res.status_code == 406:
            return "[!] WAF Detected: Server blocked the malicious request (Generic WAF)."
            
        return "[+] No WAF detected or it's well-hidden."

    except Exception as e:
        return f"[-] Error detecting WAF: {str(e)}"
