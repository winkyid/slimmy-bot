import os
import time
import requests

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}/"

offset = None

def send(chat, text):
    requests.get(API + "sendMessage", params={"chat_id": chat, "text": text})

while True:
    try:
        r = requests.get(API + "getUpdates", params={"offset": offset, "timeout": 20}).json()

        if r.get("result"):
            for upd in r["result"]:
                offset = upd["update_id"] + 1
                chat = upd["message"]["chat"]["id"]
                text = upd["message"].get("text", "")
                send(chat, f"Bot Railway aktif ➜ Kamu kirim: {text}")

    except Exception as e:
        print("Error:", e)

    time.sleep(1)
