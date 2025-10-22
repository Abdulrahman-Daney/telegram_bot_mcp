from fastmcp import FastMCP
import requests

# =========================================================
# CONFIGURATION
# =========================================================
BOT_TOKEN = "8224429854:AAH_8yihgl3HCWaUlCCTWMsEgxrOpfFk85U"  # Replace with your bot token from @BotFather

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# =========================================================
# MCP SERVER SETUP
# =========================================================
mcp = FastMCP("Telegram Bot MCP Tool")


# =========================================================
# TOOL 1: Get latest chat IDs
# =========================================================
@mcp.tool()
def get_chat_ids() -> str:
    """
    Fetch the latest Telegram messages sent to the bot and return chat IDs + sender info.
    """
    url = f"{BASE_URL}/getUpdates"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if not data.get("ok"):
            return f"❌ Telegram API error: {data.get('description', 'Unknown error')}"

        updates = data.get("result", [])
        if not updates:
            return "📭 No new messages."

        results = []
        for update in updates[-5:]:  # Get last 5 messages
            message = update.get("message", {})
            chat = message.get("chat", {})
            chat_id = chat.get("id")
            first_name = chat.get("first_name", "Unknown")
            text = message.get("text", "")
            results.append(f"💬 From {first_name} ({chat_id}): {text}")

        return "\n".join(results)

    except Exception as e:
        return f"❌ Error: {str(e)}"


# =========================================================
# TOOL 2: Send a Telegram message
# =========================================================
@mcp.tool()
def send_telegram_message(chat_id: str, message: str, parse_mode: str = "HTML") -> str:
    """
    Send a Telegram message to a specific user or group chat.
    """
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": parse_mode
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get("ok"):
            return "✅ Message sent successfully!"
        else:
            return f"❌ Telegram API error: {data.get('description', 'Unknown error')}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# =========================================================
# RUN SERVER
# =========================================================
if __name__ == "__main__":
    mcp.run(transport="streamable-http",
                    host="127.0.0.1",
                    port=8011)
