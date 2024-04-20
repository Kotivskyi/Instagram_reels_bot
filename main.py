"""Readme :  pip install python-telegram-bot --upgrade"""
from telegram import Update
from telegram.ext import *
import os
import re

BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

pattern = r"www.instagram.com/reel/"  # instagram reels pattern

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def has_instagram_reel(text):
  return re.search(pattern, text) is not None


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    message_id = update.message.message_id

    if has_instagram_reel(text):
        replaced_text = re.sub(pattern, "www.ddinstagram.com/reel/", text)
        await update.message.reply_text(replaced_text, reply_to_message_id=message_id)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    echo_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(echo_handler)
    
    application.run_polling()