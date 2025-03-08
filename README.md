# 🔐 Automated Penetration Testing Tool:

🛡 Disclaimer
⚠️ This tool is for educational & ethical hacking purposes only.
Using it without explicit permission is illegal.


A **CLI-based Ethical Hacking Tool** that automates penetration testing tasks like **port scanning, enumeration, SSH & FTP brute-force attacks** using Python & Metasploit.

## ⚡ Features
✅ **Port Scanning** – Detects open ports & running services  
✅ **Service Enumeration** – Identifies OS, services & protocols  
✅ **SSH Brute Force** – Attempts password cracking on SSH  
✅ **FTP Brute Force** – Tries multiple passwords to gain FTP access  
✅ **Metasploit Integration** – Automate exploitation (Upcoming Feature)  
✅ **Report Generation** – Saves results in `.txt`, `.csv`, and `.pdf`  

---

## 📂 Project Folder Structure

Automated-Pentest-Tool/ │── exploits/ │ ├── ssh_bruteforce.py │ ├── ftp_bruteforce.py │── scanning/ │ ├── port_scanner.py │ ├── enumeration.py │── reports/ │ ├── pentest_report.txt │── main.py │── requirements.txt │── README.md


---

## 🛠 Installation & Usage

### 🔹 **1. Install Dependencies**
```sh
pip install -r requirements.txt

2.**Run the Tool**
python main.py

📌 Usage Guide
1️⃣ Port Scanning:
python main.py
# Select Option 1 and enter target IP

2️⃣ SSH Brute Force:
python main.py
# Select Option 2 and enter target IP & username

3️⃣ FTP Brute Force:
python main.py
# Select Option 3 and enter target IP & username

4️⃣ Enumeration (OS & Services Detection):
python main.py
# Select Option 4 and enter target IP

📝 Future Enhancements
🔹 Metasploit Integration – Automate exploit execution
🔹 RDP & MySQL Brute Force – Add more attack vectors
🔹 GUI Version – Convert CLI to a GUI-based tool
🔹 Export Reports – Generate .csv & .pdf reports
