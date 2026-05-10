ReconLite Pro v2.0|Cyber Security Suite

ReconLite is a lightweight GUI-based reconnaissance and security assessment tool built for safe and authorized information gathering. It helps security researchers, students, and penetration testers perform initial target reconnaissance with an easy-to-use interface and structured reporting.

Overview

ReconLite automates the early phase of security assessment by collecting public-facing target information such as DNS records, HTTP response details, security headers, common files, and cookie configurations.

The tool is designed to be fast, lightweight, modular, and beginner-friendly while following safe reconnaissance practices.

Features

HTTP & HTTPS Target Support (Automatic Protocol Handling & Redirect Detection)

DNS Resolution (Domain to IP Mapping)

HTTP Fingerprinting (Status Code, Redirect Chain, Final URL Detection, Server Detection)

Technology Detection (Framework & Server Identification)

Security Headers Analysis

Missing Security Headers Detection

robots.txt Detection

sitemap.xml Detection

Cookie Security Inspection

JSON Report Generation

GUI-Based Interface

Modular Architecture (Easy to Extend)


Use Cases

ReconLite can be used for:

Web Application Reconnaissance

Security Posture Assessment

Bug Bounty Recon Phase

Learning Web Security Concepts

Basic Vulnerability Surface Analysis


Installation (Kali Linux / Linux)

git clone https://github.com/tehreemsate-droid/ReconLite.git
cd ReconLite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Running ReconLite

python3 main.py

Output

ReconLite generates structured JSON reports inside the output directory:

/output/target_scan.json

Report includes:

Protocol Validation (HTTP/HTTPS Status)

Redirect Tracking

DNS Information

HTTP Information

Security Headers Status

Common Files Discovery

Cookie Analysis

Scan Metadata


Project Structure

ReconLite/
├── main.py
├── modules/
├── output/
├── gui/
├── requirements.txt
└── README.md

Security Notice

ReconLite is intended only for authorized testing, learning, and research purposes. Do not scan systems without proper permission.

Future Improvements

Subdomain Enumeration

Port Scanning Integration

SSL/TLS Analysis

WHOIS Lookup

Export Reports (PDF/HTML)

Advanced Fingerprinting


Author

Tahreem

Cyber Security & Networking Enthusiast

License

This project is licensed for educational and research purposes.

 

Professional wording me add kiya gaya hai taake clear ho ke ReconLite sirf HTTP nahi, HTTPS-enabled websites bhi analyze karta hai.
Ab GitHub repo zyada complete aur polished lagega.
