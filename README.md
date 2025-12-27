

# Telegram-plugin

**Author:** reckless21  
**Version:** 0.0.1  
**Type:** extension

## Description

Telegram Bot API extension built with Flask that receives and sends messages through the Telegram Bot API. Messages can be processed and automated responses can be generated programmatically.

---

## Technology Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10+ | Core language |
| Flask | HTTP API framework |
| Requests | HTTP client for Telegram API |
| OAuth | OAuth2 handling |
| Pydantic or JSON Schema | Validation |
| OpenAPI 3.0 | Plugin interface definition |
| Shell scripting | Local execution and testing |

---

## Setup

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run locally:
```bash
python -m main
```

---

## Environment Variables

### Bot Token (`TELEGRAM_BOT_TOKEN`)

To configure this credential, you'll need a **Bot Access Token** from Telegram.

#### Generating Your Access Token:

1. **Start a chat with the BotFather**
   - Search for `@BotFather` in Telegram and start a conversation.

2. **Create a new bot**
   - Enter the `/newbot` command.

3. **Provide bot details**
   The BotFather will ask you for:
   
   - **Name:** The bot's display name in contact details and elsewhere. You can change this later.
   - **Username:** A short name used in search, mentions, and t.me links.
   
   Username requirements:
   - Must be between 5 and 32 characters long
   - Not case sensitive
   - May only include Latin characters, numbers, and underscores
   - Must end in `bot` (e.g., `tetris_bot` or `TetrisBot`)
   - Cannot be changed later

4. **Copy the bot token**
   - The BotFather will generate a token like: `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`
   - Store this securely as your `TELEGRAM_BOT_TOKEN`

**Reference:** [Telegram BotFather Documentation](https://core.telegram.org/bots#6-botfather)


---

## Available Tools

This plugin provides the following Telegram tools:

### 1. Send Message (`send_message`)

Send a plain text message to a Telegram user or chat.

**Parameters:**
- `chat_id`: Telegram chat ID or username (e.g., `123456789` or `@username`)
- `text`: Message content to send

**Example:**
```json
{
  "chat_id": "123456789",
  "text": "Hello from your bot!"
}
```


### 2. Send Template (`send_template`)

Send a pre-formatted message template to a Telegram user. This is useful for sending structured notifications or updates.

**Parameters:**
- `chat_id`: Telegram chat ID or username
- `template_name`: Name of the template to send
- `template_parameters`: Optional parameters for template variables (comma-separated or JSON array)

**Example template parameters:**
```json
{
  "chat_id": "123456789",
  "template": "Hi {{customer_name}}, your order {{order_id}} has been shipped 🚚.\n\nTracking ID: {{tracking_id}}\nExpected Delivery: {{delivery_date}}\n\nThank you for shopping with us!",
  "variables": {
    "customer_name": "Tanaya",
    "order_id": "ORD-45678",
    "tracking_id": "SHIP123456789",
    "delivery_date": "30 Dec 2025"
  }
}

```
---

## Getting Chat IDs

To send messages to groups or channels, you need the Chat ID. Here are three methods:

### Method 1: From Bot Messages
When users interact with your bot, their `chat_id` is included in the message update. You can log or store these IDs for future use.

### Method 2: From Web Browser
1. Open [Telegram Web](https://web.telegram.org/)
2. Navigate to the target group or channel
3. Check the URL: `https://web.telegram.org/k/#-1234567890`
4. The Chat ID is the number after `#` (include the minus sign for groups)

### Method 3: Using a Bot
1. Add `@userinfobot` or `@get_id_bot` to your group
2. The bot will display the Chat ID for the group
3. Remove the bot after obtaining the ID

**Note:** For groups, the Chat ID is negative (e.g., `-1234567890`)

---

## Adding Bot to Channels

For a bot to send messages to a channel, you must add it as an administrator:

1. In the Telegram app, open the target channel
2. Tap the channel name to access settings
3. Select **Administrators** → **Add Admin**
4. Search for your bot's username and select it
5. Grant necessary permissions (at minimum: "Post Messages")
6. Tap the checkmark to confirm

**Note:** You can only use `@channelusername` format with public channels. Private channels require the numeric Chat ID (with `-100` prefix).

---

## API Endpoints

The Flask application exposes the following HTTP endpoints:

- **POST /send-message**: Send a message through the bot
- **POST /send-template**: Send a message as given template

---



## Troubleshooting

### Common Issues:

**"Forbidden: bot is not a participant of the channel"**
- Solution: Add the bot as an administrator to the channel (see "Adding Bot to Channels" section)

**"Unauthorized" Error**
- Verify your bot token is correct
- Ensure the token is properly set in environment variables

**Invalid Chat ID**
- Group Chat IDs must be negative numbers
- Private channel IDs start with `-100`
- Use one of the three methods in "Getting Chat IDs" section

**Connection Timeout**
- Check your internet connection
- Verify Telegram API is accessible from your network
- Consider implementing retry logic with exponential backoff

---

## Additional Resources

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Telegram Bot Features](https://core.telegram.org/bots/features)
- [Flask Documentation](https://flask.palletsprojects.com/)

