import requests

def find_subdomains(domain):
    print(f"[*] Fetching subdomains for {domain} from public archives...")
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subdomains = set()
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomains.add(entry['name_value'].replace("*.", ""))
        
        # Sirf top 12 unique results taakay list clean aur professional rahe
        results = sorted(list(subdomains))[:12] 
        
        report = "\n" + "="*45
        report += "\n[ SUBDOMAIN ENUMERATION REPORT ]"
        report += "\n" + "="*45 + "\n"
        
        for sub in results:
            report += f"|-- [FOUND] {sub}\n"
        
        return report if results else "[-] No subdomains found in public records."
            
    except Exception as e:
        return f"[-] Subdomain Error: {str(e)}"
