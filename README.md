🚀 ReconLite Pro v2 .0|Cyber Security Suite 

Lightweight GUI-Based Reconnaissance & Security Assessment Tool

ReconLite is a lightweight GUI-based reconnaissance framework designed for safe and authorized information gathering. It helps identify public-facing target information, analyze security configurations, and generate structured reports for security assessment workflows.




🔍 Introduction

ReconLite automates the initial reconnaissance phase of web security assessment by collecting target intelligence such as DNS records, HTTP/HTTPS responses, security headers, exposed common files, and cookie configurations.

Built with a modular and scalable architecture, ReconLite separates scanning and reporting logic into independent components, making it easier to maintain and extend.

The tool is designed for students, security researchers, and penetration testers who need a fast and beginner-friendly recon workflow.




🚀 Core Features

DNS Resolution (Domain → IP Address Mapping)

HTTP & HTTPS Protocol Detection

Automatic Redirect Tracking

HTTP Fingerprinting & Server Identification

Technology Detection (Framework Discovery)

Security Headers Analysis

Missing Security Header Detection

robots.txt Discovery

sitemap.xml Detection

Cookie Security Inspection

Structured JSON Report Generation

GUI-Based Scanning Interface

Modular & Extensible Architecture




📂 Project Structure

ReconLite/
│
├── gui/               # GUI components
├── modules/           # Recon modules
├── output/            # JSON reports
├── main.py            # Application entry point
├── requirements.txt   # Dependencies
└── README.md          # Documentation




⚙️ Installation

git clone https://github.com/tehreemsate-droid/ReconLite.git
cd ReconLite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt



🧪 Usage

Run ReconLite:

python3 main.py

Enter target domain or URL through the GUI and start the reconnaissance process.




📄 Output

ReconLite generates structured JSON reports inside:

/output/

Reports include:

DNS Resolution Results

HTTP/HTTPS Status

Redirect Chain Information

Security Header Analysis

Common File Detection

Cookie Analysis

Scan Metadata





🎯 Use Cases

Web Application Reconnaissance

Initial Security Assessment

Bug Bounty Recon Phase

Learning Web Security Concepts

Surface-Level Vulnerability Analysis





⚠️ Disclaimer

ReconLite is intended strictly for educational purposes, research, and authorized testing only.

Do not scan systems without explicit permission.

Unauthorized scanning may violate legal policies.




🔮 Future Improvements

Subdomain Enumeration

Port Scanning Integration

SSL/TLS Analysis

WHOIS Lookup

HTML/PDF Export Reports

Advanced Fingerprinting





👨‍💻 Author

Tahreem
Cyber Security & Networking Enthusiast




📜 License

This project is licensed for Educational and Research Purposes.
