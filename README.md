# 🤖 Telegram AI Assistant (MCP + Dify Integration)

This project is an **AI-powered Telegram assistant** that connects through the **Telegram Bot API** using **MCP (Model Context Protocol)** and **Dify** workflow.

It allows sending and receiving messages, extracting chat IDs, and replying intelligently through automation.

---

## 🚀 Features

- Fetch recent messages and extract user `chat_id`
- Send Telegram messages easily via MCP tools
- Format messages for clear human readability
- Polite AI responses for incomplete or unrelated inputs
- Simple setup and local development support

---

## 🧩 Tech Stack

- **Python 3.10+**
- **MCP Framework**
- **Telegram Bot API**
- **Dify Workflow**

---

## ⚙️ Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/telegram-mcp-bot.git
   cd telegram-mcp-bot
   ```
   Install dependencies:

pip install -r requirements.txt

Create a .env file (based on .env.example):

BOT_TOKEN=your_telegram_bot_token_here

Run the bot:

python main.py

Integrate with Dify and use your MCP tools in the workflow.

🧪 Example Tool Descriptions

get_chat_ids: Fetches and formats recent Telegram messages.

send_telegram_message: Sends messages to a specific user or group chat.

handle_unrelated_question: Politely responds when users ask non-Telegram-related questions.

💡 Example Output

User input:

"Send a message to Daney about our new product launch!"

AI Behavior:

Finds Daney’s chat ID

Enhances the message text

Sends it automatically via Telegram API 🚀

🧑‍💻 Author

Daney
Software Engineering Student | Passionate about AI & Automation
LinkedIn
• GitHub

🏷️ License

This project is open source under the MIT License
