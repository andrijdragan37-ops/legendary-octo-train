
import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Не задано BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.reply_to(
        message,
        "Вітаємо! Це офіційний бот ОСББ «Єдність-15».\n\n"
        "Тут ви зможете отримувати оголошення та "
        "передавати звернення голові правління.\n\n"
        "Напишіть своє питання повідомленням."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(
        message,
        "Дякуємо за звернення до ОСББ «Єдність-15»! "
        "Ваше повідомлення отримано ботом."
    )

bot.infinity_polling()
