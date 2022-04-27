from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOSTNAME = 'localhost'
PORT = 8080

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(bytes('{"message": "All works good!"}', "utf-8"))

def init():
  web_server = HTTPServer((HOSTNAME, PORT), Server)
  print("Server started http://%s:%s" % (HOSTNAME, PORT))

  try:
    web_server.serve_forever()
  except KeyboardInterrupt:
    pass

  web_server.server_close()
  print("Server stopped.")

init()