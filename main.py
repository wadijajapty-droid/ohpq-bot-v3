import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# OTC Pairs List - Only these
OTC_PAIRS = [
    "EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC", "AUDUSD-OTC",
    "EURJPY-OTC", "GBPJPY-OTC", "EURGBP-OTC", "USDCAD-OTC",
    "USDCHF-OTC", "NZDUSD-OTC"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pairs_text = "\n".join([f"• {p}" for p in OTC_PAIRS])
    await update.message.reply_text(
        f"👋 OTC Analyzer Bot is LIVE\n\n"
        f"I analyze ONLY OTC pairs:\n{pairs_text}\n\n"
        f"Use: /analyze EURUSD-OTC\nOr just send: EURUSD-OTC"
    )

async def analyze_pair(pair: str):
    # --- YOUR ANALYSIS LOGIC HERE ---
    # Replace this with your real strategy
    # This is a sample response
    return f"""
📊 Analysis for {pair}:

Trend: BULLISH 🔼
Signal: BUY
Entry: Next 1 min candle
Confidence: 87%

Support: Strong
Resistance: Weak

OTC Market: Active ✅
"""

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper().strip()

    # Get pair from /analyze command or plain text
    if context.args:
        pair = context.args[0].upper()
    else:
        # Remove /analyze if present
        pair = text.replace("/ANALYZE","").strip()

    if not pair:
        await update.message.reply_text("Send me a pair like: EURUSD-OTC")
        return

    # Check if it's OTC pair only
    if pair not in OTC_PAIRS:
        await update.message.reply_text(
            f"❌ I analyze OTC ONLY.\n\nAllowed pairs:\n" + "\n".join(OTC_PAIRS)
        )
        return

    await update.message.reply_text(f"🔍 Analyzing {pair}...")

    result = await analyze_pair(pair)
    await update.message.reply_text(result)

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))

    print("Bot Started - OTC ONLY - No Screenshot")
    app.run_polling()

if __name__ == "__main__":
    main()
