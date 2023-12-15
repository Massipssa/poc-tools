import datetime as dt

from marshmallow import Schema, fields


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


if __name__ == '__main__':
    UserSchema = Schema.from_dict(
        {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
    )

    from pprint import pprint

    # Serialize
    user = User(name="Monty", email="monty@python.org")
    schema = UserSchema()
    result = schema.dump(user)
    pprint(result)

    user_data = {
        "created_at": "2014-08-11T05:26:03.869245",
        "email": "ken@yahoo.com",
        "name": "Ken",
    }

    # Deserialize
    schema = UserSchema()
    result = schema.load(user_data)
    pprint(result)
