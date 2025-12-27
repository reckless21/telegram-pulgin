from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv
from oauth import verify_api_key

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN not found in environment variable")

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

app = Flask(__name__)


def send_telegram_message(chat_id: str, text: str):
    response = requests.post(
        f"{TELEGRAM_API_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

    data = response.json()

    if not data.get("ok"):
        return {"success": False, "error": data.get("description", "Telegram API error")}

    return {"success": True, "message_id": data["result"]["message_id"]}


def render_template_message(template: str, variables: dict):
    for key, value in variables.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template



@app.route("/send-message", methods=["POST"])
def send_message():
    verify_api_key()

    payload = request.get_json()
    if not payload:
        return jsonify({"error": "Invalid JSON body"}), 400

    chat_id = payload.get("chat_id")
    text = payload.get("text")

    if not chat_id or not text:
        return jsonify({"error": "chat_id and text are required"}), 400

    result = send_telegram_message(chat_id, text)
    return jsonify(result)


@app.route("/send-template", methods=["POST"])
def send_template():
    verify_api_key()

    payload = request.get_json()
    if not payload:
        return jsonify({"error": "Invalid JSON body"}), 400

    chat_id = payload.get("chat_id")
    template = payload.get("template")
    variables = payload.get("variables", {})

    if not chat_id or not template:
        return jsonify({"error": "chat_id and template are required"}), 400

    message = render_template(template, variables)
    result = send_telegram_message(chat_id, message)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



