from http.server import BaseHTTPRequestHandler
import json
from bot import handle_update

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length)

        try:
            update = json.loads(body)
        except:
            update = {}

        handle_update(update)

        self.send_response(200)
        self.end_headers()
