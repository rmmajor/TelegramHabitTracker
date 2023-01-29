import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import Executor

from configs.env_vars import TELEGRAM_BOT_API_TOKEN
from configs import messages
# import handlers


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=True)

# dp.register_message_handler(handlers.start_handler.send_welcome, commands=['start'])

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
