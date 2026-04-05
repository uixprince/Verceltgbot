from http.server import BaseHTTPRequestHandler
import json
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def do_POST(self):
        length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(length)

        try:
            update = json.loads(body)
        except:
            update = {}

        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")

            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                json={"chat_id": chat_id, "text": f"You said: {text}"}
            )

        self.send_response(200)
        self.end_headers()
