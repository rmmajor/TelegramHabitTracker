import os
import telebot
from dotenv import load_dotenv
from configs import messages

load_dotenv()  # loads .env variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_API_TOKEN')  # retrieves token from .env

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, messages.START_COMMAND)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELP_COMMAND)


if __name__ == '__main__':
    bot.infinity_polling()
