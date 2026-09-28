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