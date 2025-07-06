import xmltodict
import networkx as nx
import matplotlib.pyplot as plt

# Load your Nmap XML output file
with open('output.xml') as fd:
    doc = xmltodict.parse(fd.read())

# Initialize NetworkX graph
G = nx.Graph()

# Dictionary to count open ports per IP for bar chart
port_counts = {}

# Parse hosts
hosts = doc['nmaprun']['host']

# Ensure hosts is a list even if single host scanned
if not isinstance(hosts, list):
    hosts = [hosts]

for host in hosts:
    ip = host['address']['@addr']
    G.add_node(ip)

    open_ports = 0

    if 'ports' in host and 'port' in host['ports']:
        ports = host['ports']['port']
        if not isinstance(ports, list):
            ports = [ports]

        for port in ports:
            portid = port['@portid']
            protocol = port['@protocol']
            service = port.get('service', {}).get('@name', 'unknown')
            state = port['state']['@state']

            # Only add if open
            if state == 'open':
                label = f"{protocol}/{portid} ({service})"
                G.add_node(label)
                G.add_edge(ip, label)
                open_ports += 1

    port_counts[ip] = open_ports

# Draw the network graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=8, font_weight='bold', edge_color='gray')
plt.title("Nmap Scan Network Topology")
plt.show()

# Draw the bar chart of open ports per IP
ips = list(port_counts.keys())
counts = list(port_counts.values())

plt.figure(figsize=(10,6))
bars = plt.bar(ips, counts, color='teal')
plt.xlabel("IP Address")
plt.ylabel("Number of Open Ports")
plt.title("Open Ports Count per IP")

# Add counts on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, int(yval), ha='center', va='bottom')

plt.tight_layout()
plt.show()
