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
        
        # Sirf top 15-20 unique results dikhayenge taakay screen bhar jaye par kachra na ho
        results = sorted(list(subdomains))[:20] 
        
        report = "\n--- [ SUBDOMAIN REPORT ] ---\n"
        for sub in results:
            report += f"|-- [FOUND] {sub}\n"
        
        return report if results else "[-] No subdomains found."
            
    except Exception as e:
        return f"[-] Subdomain Error: {str(e)}"
