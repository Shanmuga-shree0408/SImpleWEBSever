# SImpleWEBSever
# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

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
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head><title>Simple Webserver</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 80px; background-color: #f0f0f0;">
            <div style="background-color: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0px 0px 10px gray;">
                <h1>EX01 - Developing a Simple Webserver</h1>
                <h2>Name: Shanmuga Shree</h2>
                <h3>Reg No: 26017972</h3>
                <p>Webserver Running Successfully on Port 8000!</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

print("Starting server at http://localhost:8000...")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()


## OUTPUT:


## RESULT:
The program for implementing simple webserver is executed successfully.
