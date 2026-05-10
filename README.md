🚀 RECONLITE Pro v2.0|Cyber Security Suite 

⚡ Lightweight GUI-Based Reconnaissance & Security Assessment Tool

> Safe • Fast • Modular • Professional






📌 OVERVIEW

ReconLite is designed to automate the initial reconnaissance phase by collecting publicly accessible target information including DNS records, HTTP/HTTPS responses, security headers, common files, and cookie configurations.

Built for Security Researchers, Students, and Penetration Testers with a simple GUI-based workflow.




✨ FEATURES

✅ DNS Resolution — Domain to IP Mapping
✅ HTTP & HTTPS Support — Protocol Detection & Validation
✅ Redirect Detection — Final URL Tracking
✅ Server Fingerprinting — Web Server Identification
✅ Technology Detection — Framework Discovery
✅ Security Header Analysis — Header Validation
✅ Missing Header Detection — Security Misconfiguration Identification
✅ robots.txt Detection
✅ sitemap.xml Detection
✅ Cookie Security Inspection
✅ JSON Report Generation
✅ GUI-Based Interface
✅ Modular Architecture




🎯 USE CASES

✔ Web Application Reconnaissance
✔ Security Posture Assessment
✔ Bug Bounty Recon Phase
✔ Learning Web Security
✔ Initial Surface Analysis




📦 INSTALLATION

git clone https://github.com/tehreemsate-droid/ReconLite.git
cd ReconLite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt




▶ RUNNING RECONLITE

python3 main.py




📄 OUTPUT REPORTS

ReconLite generates structured JSON reports inside:

/output/target_scan.json

📊 REPORT INCLUDES

Protocol Validation (HTTP/HTTPS)

Redirect Tracking

DNS Information

HTTP Information

Security Header Status

Common Files Discovery

Cookie Analysis

Scan Metadata





🗂 PROJECT STRUCTURE

ReconLite/
├── main.py
├── modules/
├── gui/
├── output/
├── requirements.txt
└── README.md




⚠ SECURITY NOTICE

ReconLite is intended strictly for Authorized Testing, Educational Learning, and Security Research.

🚫 Do not scan unauthorized systems.




🔮 FUTURE IMPROVEMENTS

• Subdomain Enumeration
• Port Scanning Integration
• SSL/TLS Analysis
• WHOIS Lookup
• PDF/HTML Export Reports
• Advanced Fingerprinting




👨‍💻 AUTHOR

Tahreem
Cyber Security & Networking Enthusiast




📜 LICENSE

Licensed for Educational & Research Purposes.
