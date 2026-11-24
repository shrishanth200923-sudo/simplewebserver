from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocols</title>
</head>
<body>
    <h2>Register Number: 26007816</h2>
    <h2>Name: shrishanth</h2>
    <h1>List of Protocols in TCP/IP Protocol Suite</h1>
    <h3>Application Layer</h3>
    <ul>
        <li>HTTP</li><li>HTTPS</li><li>FTP</li><li>SMTP</li>
        <li>DNS</li><li>DHCP</li><li>Telnet</li><li>SSH</li>
    </ul>
    <h3>Transport Layer</h3>
    <ul>
        <li>TCP</li><li>UDP</li>
    </ul>
    <h3>Internet Layer</h3>
    <ul>
        <li>IP</li><li>ICMP</li><li>ARP</li><li>IGMP</li>
    </ul>
    <h3>Network Access Layer</h3>
    <ul>
        <li>Ethernet</li><li>PPP</li>
    </ul>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())

server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My Webserver is running on http://127.0.0.1:8000")
httpd.serve_forever()
