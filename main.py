import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Fake website for Render to keep alive
app_web = Flask(__name__)
@app_web.route('/')
def home():
    return "Bot is LIVE!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host='0.0.0.0', port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive! Use /signal")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # add your other handlers here
    print("Bot polling started...")
    app.run_polling()

if __name__ == "__main__":
    # Start web in background
    threading.Thread(target=run_web, daemon=True).start()
    # Start bot in main thread (important!)
    run_bot()
