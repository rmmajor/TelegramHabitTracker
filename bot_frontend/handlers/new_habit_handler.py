import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from configs import messages
from bot_frontend.bot import dp


# States
class NewHabitForm(StatesGroup):
    name = State()
    fire_at = State()
    # habit_start = State()
    # repeat_times = State()


# @dp.message_handler(commands=['new_habit'])
async def new_habit_registration_start(message: types.Message):
    """
    Entry point for registering new habit

    """
    # sets state
    await NewHabitForm.name.set()

    await message.reply(messages.NEW_HABIT_COMMAND)


# @dp.message_handler(state=NewHabitForm.name)
async def process_new_habit_name(message: types.Message, state: FSMContext):
    """
    Process habit name, and asks for time
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await NewHabitForm.next()
    await message.reply(messages.HABIT_REGISTRATION_STEP_1)


# @dp.message_handler(state=NewHabitForm.fire_at)
async def process_new_habit_fire_time(message: types.Message, state: FSMContext):
    """
    Process habit time
    """
    async with state.proxy() as data:
        data['fire_at'] = message.text

    await message.reply(f"Нову звичку {data['name']} створено успішно! \n"
                        f"Тепер Вам щодня о {data['fire_at']} буде приходити сповіщення")

    # Finish conversation
    await state.finish()


def register_new_habit_handler(dp: Dispatcher):
    dp.register_message_handler(new_habit_registration_start, commands=['new_habit'])
    dp.register_message_handler(process_new_habit_name, state=NewHabitForm.name)
    dp.register_message_handler(process_new_habit_fire_time, state=NewHabitForm.fire_at)

