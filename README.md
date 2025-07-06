<h1 align="center">🛡️🔍 Nmap Visualization with Python</h1>

<p align="center">
Transforming raw Nmap scans into actionable, beautiful visual insights.
</p>

<p align="center">
  <a href="https://github.com/MinishaMuthukumar/nmap-visualization">
  </a>
</p>

---

## ✨ **About This Project**

This tool parses **Nmap XML scan outputs** and generates:

- 🌐 **Network Topology Graph** – Visualizes IP addresses with their open ports/services  
- 📊 **Bar Chart** – Shows the number of open ports per host for quick analysis

---

## 🚀 **Why use this?**

Traditional Nmap outputs are powerful but text-heavy. Visualizing them:

✅ Helps **penetration testers** understand attack surfaces quickly  
✅ Enables **network admins** to identify exposures clearly

---

## 🛠 **Built With**

- 🐍 Python
- 📦 xmltodict
- 🖧 NetworkX
- 📈 Matplotlib

---

## ⚡ **Step-by-Step Procedure**

### **🔧 1. Prerequisites**

Ensure you have:

✅ **Python installed** (Python 3.8+)  
✅ **Nmap installed** (default on Kali Linux)

Install required Python libraries:

```bash


pip install xmltodict networkx matplotlib
🔎 2. Perform Nmap Scan
Run your Nmap scan with XML output:


nmap -sV -oX output.xml <target-ip-or-range>

✔️ Replace <target-ip-or-range> with your target IP or subnet.
✔️ This generates an output.xml file containing the scan results.

💻 3. Clone this Repository


git clone https://github.com/MinishaMuthukumar/nmap-visualization.git

cd nmap-visualization

📂 4. Add Your Nmap Output
Place your output.xml file inside this project folder.

🚀 5. Run the Visualization Script
Run the Python script to visualize your scan:


python nmap_visualize.py
👀 6. View Outputs
You will see:

🌐 Network Topology Graph Window – showing IPs and their open ports/services

📊 Bar Chart Window – showing number of open ports per IP



Vulnerability visualization using Nmap NSE scripts

Interactive dashboard with Streamlit

👩‍💻 Author
👤 Minisha Muthukumar
💡 B.Tech IT | Cybersecurity & Ethical Hacking Enthusiast

