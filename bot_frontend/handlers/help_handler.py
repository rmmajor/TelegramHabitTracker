from aiogram import types, Dispatcher
from configs import messages


async def send_help(message: types.Message):

    await message.reply(messages.HELP_COMMAND)


def register_help_handler(dp: Dispatcher):
    dp.register_message_handler(send_help, commands=['help'])
