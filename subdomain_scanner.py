import requests
import re

def find_subdomains(domain):
    print(f"\n[*] Enumerating subdomains for: {domain}")
    subdomains = set()
    
    # Using crt.sh (Passive Enumeration - Industry Standard)
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name = entry['name_value']
                # Cleaning the output
                if "\n" in name:
                    parts = name.split("\n")
                    for p in parts:
                        subdomains.add(p.replace("*.", ""))
                else:
                    subdomains.add(name.replace("*.", ""))
        
        # Displaying top 10 unique subdomains
        results = sorted(list(subdomains))[:10]
        if results:
            return f"[+] Found {len(subdomains)} subdomains. Top results: " + ", ".join(results)
        else:
            return "[-] No subdomains found via passive scan."
            
    except Exception as e:
        return f"[-] Subdomain Scan Error: {str(e)}"
