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
    user_schema.telegram_id = telegram_id
    user_schema.created_at = datetime.now()
    schema_to_load = dict(user_schema)

    print(type(schema_to_load), type(user_data))

    try:
        new_user = create_entry(BotUser, **schema_to_load)
    except sqlalchemy.exc.IntegrityError:
        pass
