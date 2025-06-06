#PS: Šitas skriptas pilnai sukurtas AI)
from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello to Code Academy"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    server_address = ("", 8000)  # Listen on port 8000
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
