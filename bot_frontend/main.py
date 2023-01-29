from bot import executor, dp
from handlers import help_handler, start_handler, cancel_handler, new_habit_handler

help_handler.register_help_handler(dp)
start_handler.register_start_handler(dp)
cancel_handler.register_cancel_handler(dp)
new_habit_handler.register_new_habit_handler(dp)


if __name__ == '__main__':
    executor.start_polling()
