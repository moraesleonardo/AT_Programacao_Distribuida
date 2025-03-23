from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8080
Handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando na porta {PORT}...")
    httpd.serve_forever()

