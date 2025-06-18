
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils import get_btc_status, get_levels, get_rsi, get_news

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привіт! Я BTC Sig Bot. Команди: /status, /levels, /rsi, /news")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_btc_status())

async def levels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_levels())

async def rsi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_rsi())

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_news())

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("levels", levels))
app.add_handler(CommandHandler("rsi", rsi))
app.add_handler(CommandHandler("news", news))

if __name__ == "__main__":
    app.run_polling()
