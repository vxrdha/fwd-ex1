# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

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
~~~
from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''
<!DOCTYPE html>
<html>f
<head>
  <title>TCP/IP Protocol Table</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #444;
      padding: 10px;
      text-align: center;
    }
    th {
      background-color: #2980b9;
      color: white;
    }
    caption {
      font-size: 1.5em;
      margin-bottom: 10px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <table>
    <caption>TCP/IP Protocol Suite</caption>
    <tr>
      <th>Layer</th>
      <th>Function</th>
      <th>Common Protocols</th>
    </tr>
    <tr>
      <td>Application</td>
      <td>Provides services to user applications</td>
      <td>HTTP, FTP, SMTP, DNS, DHCP, SNMP</td>
    </tr>
    <tr>
      <td>Transport</td>
      <td>Reliable or fast data transmission</td>
      <td>TCP, UDP</td>
    </tr>
    <tr>
      <td>Internet</td>
      <td>Routing and logical addressing</td>
      <td>IP, ICMP, ARP, RARP</td>
    </tr>
    <tr>
      <td>Network Access</td>
      <td>Physical data transmission</td>
      <td>Ethernet, Wi-Fi, PPP</td>
    </tr>
  </table>
</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
~~~


## OUTPUT:
![alt text](<Screenshot 2025-09-19 203956.png>)
![alt text](<Screenshot 2025-09-19 204032.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

