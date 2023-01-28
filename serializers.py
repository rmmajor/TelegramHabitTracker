from marshmallow import Schema, fields


class NewUser(Schema):
    telegram_id = fields.Integer()
    created_at = fields.DateTime()


class NewHabit(Schema):

    name = fields.String()
    fire_at = fields.Time()
    habit_start = fields.Date()
    repeat_times = fields.Integer()

    consistency_id = fields.Integer()
    user_id = fields.Integer()


class NewConsistency(Schema):

    each = fields.Integer(default=1)
    # type = Column(
    #     'type',
    #     sqlalchemy.Enum('hour', 'day', 'week', 'month', 'year',
    #                     name='consistency_types',
    #                     create_type=False)
    # )

    sunday = fields.Boolean(default=False)
    monday = fields.Boolean(default=False)
    tuesday = fields.Boolean(default=False)
    wednesday = fields.Boolean(default=False)
    thursday = fields.Boolean(default=False)
    friday = fields.Boolean(default=False)
    saturday = fields.Boolean(default=False)


