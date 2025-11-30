🔍 Python Port Scanner

A fast, multi-threaded, and beginner-friendly TCP Port Scanner built using Python.
It scans a target IP/domain for open ports using lightweight socket connections and threads to maximize speed.

🚀 Features

⚡ Multithreaded scanning (super fast)

🎛 Custom port range (default: 1–1024)

📊 Progress bar using tqdm

🧩 Clean modular structure (utils.py, scanner.py, main.py)

🖥 CLI-based interface

📦 Very lightweight — uses only Python’s standard library

🛡 Perfect for cybersecurity beginners

📁 Project Structure
port-scanner/
│
├── main.py          # CLI interface & entry point
├── scanner.py       # Threaded port scanning logic
├── utils.py         # Socket connection helper
├── requirements.txt # Project dependencies
└── README.md        # Documentation

🛠️ Installation

Make sure you have Python 3.x installed.

git clone https://github.com/<your-username>/port-scanner.git
cd port-scanner
pip install -r requirements.txt

▶️ Usage

Run the scanner with:

python main.py <target> --start <start_port> --end <end_port> --threads <count>

Example Scan

Scan ports 1–1024 on localhost:

python main.py 127.0.0.1 --start 1 --end 1024 --threads 200

Output Example
🔍 Scanning Target: 127.0.0.1
📌 Port Range: 1 → 1024
⚡ Threads Used: 200

🟢 OPEN PORT: 22
🟢 OPEN PORT: 80
🟢 OPEN PORT: 443

🎯 Scan Completed!
=================================
🔓 Open Ports Found:
 → 22
 → 80
 → 443

📦 Dependencies
tqdm


Installed automatically through requirements.txt.

🧪 Testing the Scanner

To test locally:

Start a temporary HTTP server:

python -m http.server 8080


Scan your machine:

python main.py 127.0.0.1 --start 1 --end 9000


You should see:

🟢 OPEN PORT: 8080

⚠️ Legal Disclaimer

This project is for educational and ethical cybersecurity research only.
Scanning systems without permission is illegal and punishable by law.
Use this tool only on systems you own or have explicit authorization to test.

⭐ Future Improvements

Banner grabbing

Service detection

Scan report (JSON/CSV)

Async (ultra-fast) version

GUI version

🙌 Contributions

Pull requests are welcome!
Feel free to fork this repository and improve the tool.

📄 License

MIT License — free to use, modify, and distribute.