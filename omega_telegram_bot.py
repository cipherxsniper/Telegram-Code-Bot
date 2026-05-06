cat > omega_telegram_bot.py << 'EOF'
import requests
from omega_router import route
from omega_config import TELEGRAM_BOT_TOKEN

URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    })

def get_updates(offset=None):
    return requests.get(f"{URL}/getUpdates", params={"offset": offset}).json()

def main():
    print("🧠 Omega AI Bot Running (Core UI v2)")

    offset = None

    while True:
        data = get_updates(offset)

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text")

            if not text:
                continue

            response = route(text)
            send(chat_id, response)

if __name__ == "__main__":
    main()
EOF
