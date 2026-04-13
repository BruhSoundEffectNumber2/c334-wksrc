from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8000

def hello():
    return "Hello, World!"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(hello().encode())

class Server(HTTPServer):
     allow_reuse_address = True


if __name__ == "__main__":
    try:
        with Server(("", PORT), Handler) as httpd:
                print(f"Serving at port {PORT}")
                httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")