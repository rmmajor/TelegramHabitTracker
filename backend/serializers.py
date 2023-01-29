from marshmallow import Schema, fields, validate


class NewUser(Schema):
    telegram_id = fields.Integer()  # add unique validation
    created_at = fields.DateTime()


class NewHabit(Schema):

    name = fields.String(required=True)
    fire_at = fields.Time(required=True)
    habit_start = fields.Date()  # current day
    repeat_times = fields.Integer()

    consistency_id = fields.Integer()
    user_id = fields.Integer()


class NewConsistency(Schema):

    each = fields.Integer(default=1)
    type = fields.String(validate=validate.OneOf(['hour', 'day', 'week', 'month', 'year']))
    sunday = fields.Boolean(default=False)
    monday = fields.Boolean(default=False)
    tuesday = fields.Boolean(default=False)
    wednesday = fields.Boolean(default=False)
    thursday = fields.Boolean(default=False)
    friday = fields.Boolean(default=False)
    saturday = fields.Boolean(default=False)


