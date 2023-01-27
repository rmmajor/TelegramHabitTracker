import telebot
from configs import messages, env_vars

bot = telebot.TeleBot(env_vars.TELEGRAM_BOT_API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, messages.START_COMMAND)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELP_COMMAND)


@bot.message_handler(commands=['new_habit'])
def send_welcome(message):
    bot.reply_to(message, messages.NEW_HABIT_COMMAND)


if __name__ == '__main__':
    bot.infinity_polling()
