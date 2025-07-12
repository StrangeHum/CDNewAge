from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# import os
# from dotenv import load_dotenv

TOKEN = "6251377163:AAGHocnHBFunewuf0S_D3aOexRfkhxCIsSo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот готов принимать сообщения!")

def create_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print('Telegramm bot has been runned')
    return app

# create_bot().run_polling()