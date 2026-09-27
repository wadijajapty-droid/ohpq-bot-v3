import os
from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("OHPQ V3 LIVE 🚀")

def main():
    if not TOKEN:
        print("No token")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
