from aiogram import types, Dispatcher

from bot_frontend import bot_utils
from configs import messages


async def send_welcome(message: types.Message):
    bot_utils.register_user(message.from_user.id)
    await message.reply(messages.START_COMMAND)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
