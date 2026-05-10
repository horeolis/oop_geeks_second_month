from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"


# функция обработки сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_text("Привет 👋")

    elif "как дела" in text:
        await update.message.reply_text("Нормально, я бот 🤖")

    elif "кто ты" in text:
        await update.message.reply_text("Я простой Telegram-бот")

    elif "пока" in text:
        await update.message.reply_text("Пока 👋")

    else:
        await update.message.reply_text("Я тебя не понял 🤔")


# запуск приложения
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")

app.run_polling()