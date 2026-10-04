# Account Validation Tool (Patched)
A multi-threaded account validation tool built in Python for testing HTTP requests, bypassing Cloudflare protections using cloudscraper, and interacting with Riot Games/KeyAuth APIs.

## 🛠️ Prerequisites & Installation
This project relies on several standard and third-party libraries. Run the command below to install all necessary external dependencies:

```bash
pip install requests cloudscraper easygui pandas colorama httpx aiohttp readchar
```

## 🚀 Key Features
Cloudflare Bypass: Integrates cloudscraper to navigate Cloudflare anti-bot checks during HTTP requests.

Asynchronous & Multi-threaded Architecture: Uses asyncio, aiohttp, httpx, and Python's threading library for high-concurrency request handling.

Terminal UI: Color-coded console output provided by colorama.

Data Processing & File Handling: Built-in support for data manipulation via pandas and GUI dialogs via easygui.

Custom Customizations: Customized TLS adapter configurations using urllib3 and ssl for low-level network request management.
```consloe
📁 File Structure
├── main.py               # Main application entry point
├── keyauth.py            # KeyAuth API integration
├── riotchecker.py        # Proxy Checker for Riot Games API
└── valx/                 # Additional validation utilities
```
## 💻 Usage
Open a terminal in the root directory.

Execute the main script:
```bash
python main.py
```

## ⚠️ Disclaimer
This tool is designed for educational and authorized testing purposes only. Usage of this software for unauthorized testing or malicious activities is strictly prohibited.
