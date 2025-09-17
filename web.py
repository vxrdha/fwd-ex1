from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Display Public IP Address</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background-color: #f4f4f4;
    }
    .ip-box {
      background-color: #fff;
      padding: 20px;
      border-radius: 6px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      max-width: 400px;
      margin: auto;
      text-align: center;
    }
    .ip-address {
      font-size: 1.5em;
      color: #333;
    }
  </style>
</head>
<body>

  <div class="ip-box">
    <h2>Your Public IP Address is:</h2>
    <p class="ip-address" id="ip">Loading...</p>
  </div>

  <script>
    // Fetch the user's public IP using ipify API
    fetch('https://api.ipify.org?format=json')
      .then(response => response.json())
      .then(data => {
        document.getElementById('ip').textContent = data.ip;
      })
      .catch(error => {
        document.getElementById('ip').textContent = 'Unable to fetch IP.';
        console.error('Error fetching IP:', error);
      });
  </script>

</body>
</html>


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
