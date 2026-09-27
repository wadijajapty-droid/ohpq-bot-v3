import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("OHPQ V3 LIVE - Fixed Python 3.11 🚀\nTap /start again in 50s if I sleep")

def main():
    if not TOKEN:
        print("No BOT_TOKEN set")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot starting polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
