from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CallbackQueryHandler,  # ← вот это добавь
    ContextTypes,
    filters,
)
import requests
import random
from datetime import datetime


TOKEN = "8708744453:AAFbrYISORkpfzhQjXLb9oXYvTgQakallL8"
WEATHER_API_KEY = "57769c6a72b20949293c9d9bd319a6b6"
async def get_weather(city: str) -> str:
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        return "Город не найден 🤔"

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    city_name = data["name"]

    return f"🌤 Погода в {city_name}:\n{desc}\n🌡 {temp}°C, ощущается как {feels}°C"


# главное меню с кнопками
async def send_menu(update: Update):
    keyboard = [
        [InlineKeyboardButton("🌤 Погода", callback_data="weather")],
        [InlineKeyboardButton("🔮 Предсказание", callback_data="predict")],
        [InlineKeyboardButton("🧠 Аутизм mode", callback_data="autism")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери что хочешь:", reply_markup=reply_markup)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_text("Привет 👋")
        await send_menu(update)  # показываем кнопки

    elif "погода" in text:
        weather = await get_weather("Bishkek")
        await update.message.reply_text(weather)

    elif "как дела" in text:
        await update.message.reply_text("Нормально, я бот 🤖")

    elif "кто ты" in text:
        await update.message.reply_text("Я простой Telegram-бот")

    elif "пока" in text:
        await update.message.reply_text("Пока 👋")

    elif "предскажи" in text:
        answers = [
            "Однозначно да ✅",
            "Не думаю ❌",
            "Возможно 🤔",
            "Лучше не знать 😅",
            "Звёзды говорят да 🌟",
            "Даже не мечтай 😂"
        ]
        await update.message.reply_text(random.choice(answers))

    elif "меню" in text:
        await send_menu(update)

    else:
        await update.message.reply_text("Ты пидор, чмо, хуесос и молодец и пакистанец")


# обработчик нажатий на кнопки
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # убирает "часики" на кнопке

    if query.data == "weather":
        weather = await get_weather("Bishkek")
        await query.message.reply_text(weather)

    elif query.data == "predict":
        answers = [
            "Однозначно да ✅",
            "Не думаю ❌",
            "Возможно 🤔",
            "Лучше не знать 😅",
            "Звёзды говорят да 🌟",
            "Даже не мечтай 😂"
        ]
        await query.message.reply_text(random.choice(answers))

    elif query.data == "autism":
        # кнопки да/нет для собаки
        keyboard = [
            [
                InlineKeyboardButton("Да 🐶", callback_data="dog_yes"),
                InlineKeyboardButton("Нет 🤔", callback_data="dog_no"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Это собака?")
        await query.message.reply_photo(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBgbJbDI7rsSWbz-Kjzgqkp2w97yWzg6BtOg&s",
            reply_markup=reply_markup
        )

    elif query.data == "dog_yes":
        await query.message.reply_text("Правильно! 🐶")

    elif query.data == "dog_no":
        await query.message.reply_text("Ты конч? Это явно собака 🐕")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(CallbackQueryHandler(handle_buttons))  # обработчик кнопок
print("Бот робит")
app.run_polling()    







