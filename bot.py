import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")

def send_message(chat_id, text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )

def handle_update(update):
    if "message" in update:
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            send_message(chat_id, "Bot working ✅")

        elif text == "/help":
            send_message(chat_id, "Available commands: /start /help")

        else:
            send_message(chat_id, f"You said: {text}")
