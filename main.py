import os, threading
from flask import Flask

# --- FAST KEEP-ALIVE SERVER ---
app = Flask(__name__)
@app.route('/')
def home():
    return "OHPQ BOT V3 - FAST & ONLINE"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_web, daemon=True).start()

# --- YOUR BOT LOGIC STARTS HERE ---
# Paste your original bot code below this line
# If you use Baileys/WhatsApp, keep it light - no heavy loops

print("OHPQ BOT V3 Starting FAST...")
# Example: import your bot handler
# import bot_handler
# bot_handler.start()

# Keep bot alive
import time
while True:
    time.sleep(10)
