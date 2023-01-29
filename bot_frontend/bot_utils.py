from backend.serializers import NewUser
from datetime import datetime
from backend.db_utils import *
import sqlalchemy


def register_user(telegram_id):
    user_data = {
        'telegram_id': telegram_id,
        'created_at': str(datetime.now())
    }

    user_schema = NewUser()
    schema_to_load = user_schema.load(user_data)

    try:
        new_user = create_entry(BotUser, **schema_to_load)
    except sqlalchemy.exc.IntegrityError:
        print("user already exists")
