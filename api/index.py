from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request

TOKEN = os.environ.get("BOT_TOKEN")

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_POST(self):
        try:
            length = int(self.headers.get('content-length', 0))
            body = self.rfile.read(length)
            update = json.loads(body)

            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                reply = "You said: " + text

                url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                data = json.dumps({
                    "chat_id": chat_id,
                    "text": reply
                }).encode()

                req = urllib.request.Request(
                    url,
                    data=data,
                    headers={"Content-Type": "application/json"}
                )
                urllib.request.urlopen(req)

        except Exception as e:
            print(e)

        self.send_response(200)
        self.end_headers()
