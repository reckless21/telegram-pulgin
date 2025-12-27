📬 Telegram Messaging Plugin

Version: 1.0.0

Type: Extension / Plugin

📖 Description

The Telegram Messaging Plugin enables sending messages to Telegram users and groups using the Telegram Bot API.

This plugin exposes HTTP endpoints that can be used by automation platforms to:

Send plain text messages

Send template-based messages with dynamic variables

The plugin acts as a lightweight gateway between your system and Telegram.

⚙️ Setup & Installation
1. Install dependencies
pip install -r requirements.txt

2. Environment Variables

Create a .env file in the project root:

TELEGRAM_BOT_TOKEN=123456789:AAxxxxxxxxxxxxxxxxxxxxxxxx
PLUGIN_API_KEY=your_internal_plugin_key

🔐 Environment Variables Explained
Variable	Description
TELEGRAM_BOT_TOKEN	Bot token generated using @BotFather on Telegram
PLUGIN_API_KEY	Optional security key used to restrict API access (internal use only)
🤖 Creating a Telegram Bot

Open Telegram and search for @BotFather

Run /start

Create a bot using /newbot

Copy the Bot Token

Paste it into your .env file

🧩 Plugin Capabilities
1️⃣ Send Message (send-message)

Send a plain text message to a Telegram user or group.

Endpoint

POST /send-message


Request Body

{
  "chat_id": "123456789",
  "text": "Hello from Telegram Plugin"
}

2️⃣ Send Template Message (send-template)

Send a dynamic template-based message.

Endpoint

POST /send-template


Request Body

{
  "chat_id": "123456789",
  "template": "Hello {{name}}, your order {{order_id}} is ready.",
  "variables": {
    "name": "John",
    "order_id": "ORD123"
  }
}

🧠 How Template Messages Work

The plugin replaces placeholders using double curly braces:

{{name}} → "John"
{{order_id}} → "ORD123"


This allows dynamic personalization without changing message structure.

📡 How to Get Telegram Chat ID
Option 1: Using @userinfobot

Open Telegram

Search @userinfobot

Click Start

Copy your Chat ID

Option 2: Using Bot Interaction

Start your bot

Send any message

Call:

https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates


Extract chat.id

🚀 Running the Plugin
python app.py


Server runs at:

http://localhost:8000

🧪 Testing the Plugins
via Using CURL
curl -X POST http://127.0.0.1:8000/send-message \
  -H "Content-Type: application/json" \
  -d '{
    "chat_id": "123456789",
    "text": "Hello from Telegram plugin!"
  }'
