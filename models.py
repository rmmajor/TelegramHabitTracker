from sqlalchemy import create_engine, Column, ForeignKey
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from configs.env_vars import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


connection_string = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_engine(connection_string)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
Base = declarative_base()


class BotUser(Base):
    __tablename__ = "bot_user"

    telegram_id = Column('telegram_id', sqlalchemy.BigInteger, primary_key=True)
    created_at = Column('created_at', sqlalchemy.TIMESTAMP, nullable=False)


class Consistency(Base):
    __tablename__ = "consistency"

    """"
    Model for setting consistency settings, for example, if
    each=2, type='week', tuesday = True, it means that each second tuesday the habit will be triggered. 
    """

    id = Column('id', sqlalchemy.Integer, primary_key=True)
    each = Column('each', sqlalchemy.Integer, nullable=False, default=1)
    type = Column(
        'type',
        sqlalchemy.Enum('hour', 'day', 'week', 'month', 'year',
                        name='consistency_types',
                        create_type=False)
    )
    sunday = Column('sunday', sqlalchemy.Boolean, default=False)
    monday = Column('monday', sqlalchemy.Boolean, default=False)
    tuesday = Column('tuesday', sqlalchemy.Boolean, default=False)
    wednesday = Column('wednesday', sqlalchemy.Boolean, default=False)
    thursday = Column('thursday', sqlalchemy.Boolean, default=False)
    friday = Column('friday', sqlalchemy.Boolean, default=False)
    saturday = Column('saturday', sqlalchemy.Boolean, default=False)


class Habit(Base):
    __tablename__ = "habit"

    id = Column('id', sqlalchemy.Integer, primary_key=True)
    name = Column('name', sqlalchemy.String, nullable=False)
    fire_at = Column('fire_at', sqlalchemy.TIME, nullable=False)
    habit_start = Column('habit_start', sqlalchemy.DATE, nullable=False)
    repeat_times = Column('repeat_times', sqlalchemy.Integer, nullable=True)  # when null, repeat forever

    consistency_id = Column('habit_id', ForeignKey(Consistency.id))
    user_id = Column('user_id', ForeignKey(BotUser.telegram_id))


class HabitTracks(Base):
    __tablename__ = "habit_tracks"

    id = Column('id', sqlalchemy.Integer, primary_key=True)
    is_success = Column('is_success', sqlalchemy.Boolean, default=False, nullable=False)
    XP_change = Column('XP_change', sqlalchemy.Integer, nullable=True)
    done_at = Column('done_at', sqlalchemy.TIMESTAMP, nullable=False)

    habit_id = Column('habit_id', ForeignKey(Habit.id))
