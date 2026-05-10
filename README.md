🚀 ReconLite Pro v2.0|Cyber Security Suite

> Lightweight GUI-based Reconnaissance & Security Assessment Tool for safe and authorized information gathering.





📌 Overview

ReconLite is designed to automate the initial phase of reconnaissance by collecting publicly accessible target information such as DNS records, HTTP/HTTPS details, security headers, common files, and cookie configurations.

It provides a fast, lightweight, and beginner-friendly GUI interface for security researchers, students, and penetration testers.



✨ Features

✔ DNS Resolution — Domain to IP Mapping
✔ HTTP & HTTPS Support — Automatic Protocol Handling
✔ Redirect Detection — Tracks Final URL Path
✔ HTTP Fingerprinting — Status Code & Server Detection
✔ Technology Detection — Framework Identification
✔ Security Headers Analysis
✔ Missing Security Header Detection
✔ robots.txt Detection
✔ sitemap.xml Detection
✔ Cookie Security Inspection
✔ Structured JSON Report Generation
✔ GUI-Based Interface
✔ Modular Architecture (Easy to Extend)


🎯 Use Cases

Web Application Reconnaissance

Security Posture Assessment

Bug Bounty Recon Phase

Learning Web Security Concepts

Basic Vulnerability Surface Analysis


📦 Installation (Kali Linux / Linux)

git clone https://github.com/tehreemsate-droid/ReconLite.git
cd ReconLite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


▶ Running ReconLite

python3 main.py


📄 Output

ReconLite generates structured JSON reports inside the output directory:

/output/target_scan.json

Report Includes:

Protocol Validation (HTTP/HTTPS Status)

Redirect Tracking

DNS Information

HTTP Information

Security Headers Status

Common Files Discovery

Cookie Analysis

Scan Metadata



🗂 Project Structure

ReconLite/
├── main.py
├── modules/
├── output/
├── gui/
├── requirements.txt
└── README.md



⚠ Security Notice

ReconLite is intended only for authorized testing, educational learning, and research purposes.

Do not scan systems without proper permission.


🔮 Future Improvements

Subdomain Enumeration

Port Scanning Integration

SSL/TLS Analysis

WHOIS Lookup

PDF/HTML Export Reports

Advanced Fingerprinting




👨‍💻 Author

Tahreem
Cyber Security & Networking Enthusiast




📜 License

This project is licensed for educational and research purposes.
