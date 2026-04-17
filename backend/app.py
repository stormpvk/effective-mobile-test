from http.server import HTTPServer, BaseHTTPRequestHandler
 
class SimpleHttpServer(BaseHTTPRequestHandler):
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))
 
hostName = "0.0.0.0"
serverPort = 8080
 
webServer = HTTPServer((hostName, serverPort), SimpleHttpServer)
webServer.serve_forever()
webServer.server_close()