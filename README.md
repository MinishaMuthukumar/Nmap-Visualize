<h1 align="center">🛡️🔍 Nmap Visualization with Python</h1>

<p align="center">
Transforming raw Nmap scans into actionable, beautiful visual insights.
</p>

<p align="center">
  <a href="https://github.com/MinishaMuthukumar/nmap-visualization">
    <img src="https://img.shields.io/github/stars/MinishaMuthukumar/nmap-visualization?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/MinishaMuthukumar/nmap-visualization/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/MinishaMuthukumar/nmap-visualization" alt="License">
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
