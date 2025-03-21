from http.server import SimpleHTTPRequestHandler, HTTPServer
import json  # Importando o módulo json

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Servir arquivos estáticos (CSS, JS) diretamente
        if self.path == '/api/dados':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'mensagem': 'API funcionando!'}
            self.wfile.write(json.dumps(response).encode())  # Usando json.dumps() para gerar o JSON
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('frontend/index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('frontend/style.css', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Servidor rodando em http://localhost:8000')
    httpd.serve_forever()
