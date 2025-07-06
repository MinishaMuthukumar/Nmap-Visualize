<h1 align="center">🛡️🔍 Nmap Visualization with Python</h1>

<p align="center">
Transforming raw Nmap scans into actionable, beautiful visual insights.
</p>

---

<h2>✨ About This Project</h2>

<p>This tool parses <b>Nmap XML outputs</b> to generate:</p>

<ul>
  <li>🌐 <b>Network Topology Graph</b> – Visualize IPs and their open ports/services</li>
  <li>📊 <b>Bar Chart</b> – See the number of open ports per host at a glance</li>
</ul>

---

<h2>🚀 Why?</h2>

<p>Traditional Nmap outputs are powerful but text-heavy. This project helps:</p>

<ul>
  <li>✅ <b>Penetration testers</b> understand attack surfaces quickly</li>
  <li>✅ <b>Network admins</b> identify exposures and plan remediation</li>
</ul>

---

<h2>🛠 Built With</h2>

<ul>
  <li>🐍 Python</li>
  <li>📦 xmltodict</li>
  <li>🖧 NetworkX</li>
  <li>📈 Matplotlib</li>
</ul>

---

<h2>⚡ How To Run</h2>

<ol>
  <li><b>Run Nmap scan</b> with XML output:
    <pre>
nmap -sV -oX output.xml &lt;target-ip-or-range&gt;
    </pre>
  </li>

  <li><b>Place <code>output.xml</code></b> in your project folder.</li>

  <li><b>Run the script:</b>
    <pre>
python nmap_visualize.py
    </pre>
  </li>

  <li><b>View the outputs:</b>
    <ul>
      <li>🌐 Network graph window</li>
      <li>📊 Bar chart window</li>
    </ul>
  </li>
</ol>

---

<h2>💡 Example Visuals</h2>

<table>
  <tr>
    <th>Network Graph</th>
    <th>Bar Chart</th>
  </tr>
  <tr>
    <td align="center">
      <img src="images/network_graph.png" width="300"/>
    </td>
    <td align="center">
      <img src="images/bar_chart.png" width="300"/>
    </td>
  </tr>
</table>

<p><i>Add screenshots to your <code>/images</code> folder for better README presentation.</i></p>

---

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Service heatmaps</li>
  <li>Vulnerability visualizations using Nmap NSE scripts</li>
  <li>Interactive dashboard with Streamlit</li>
</ul>

---

<h2>👩‍💻 Author</h2>

<p>
👤 <a href="https://github.com/MinishaMuthukumar">Minisha Muthukumar</a><br>
💡 B.Tech IT | Cybersecurity & Ethical Hacking Enthusiast
</p>

---

<p align="center">
⭐️ <b>If you find this project useful, please star this repo!</b>
</p>
