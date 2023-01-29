import telebot
from configs import messages, env_vars
import bot_utils


bot = telebot.TeleBot(env_vars.TELEGRAM_BOT_API_TOKEN)


@bot.message_handler(commands=['new_habit'])
def send_welcome(message):
    get_habit_name_msg = bot.reply_to(message, messages.NEW_HABIT_COMMAND)
    bot.register_next_step_handler(get_habit_name_msg, process_habit_name_step)


def process_habit_name_step(message):
    habit_name = message.text
    print(habit_name)
    bot.reply_to(message, messages.HABIT_REGISTRATION_STEP_1)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.from_user.id)
    bot_utils.register_user(message.from_user.id)
    bot.reply_to(message, messages.START_COMMAND)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELP_COMMAND)


if __name__ == '__main__':
    bot.infinity_polling()
