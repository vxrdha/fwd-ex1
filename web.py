from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
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

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
