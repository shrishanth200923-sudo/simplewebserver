# EX01 Developing a Simple Webserver
## Date:24.11.2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

```python
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
```
## OUTPUT:
<img width="1085" height="863" alt="image" src="https://github.com/user-attachments/assets/e9ddd43c-cf17-4c43-b7a3-0aa82b9d89fb" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/0a811cdb-a808-4871-a939-b9cb54d07028" />



## RESULT:
The program for implementing simple webserver is executed successfully.
