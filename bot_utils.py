import json

from serializers import NewUser
from models import BotUser
from datetime import datetime
from db_utils import *


def register_user(telegram_id):
    user_data = {
        'telegram_id': telegram_id,
        'created_at': str(datetime.now())
    }

    user_schema = NewUser()
    shema_to_load = user_schema.load(user_data)

    new_user = create_entry(BotUser, **shema_to_load)

