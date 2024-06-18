import enum

from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    """User validation schema"""
    password_validator = [
        validate.Length(min=5, max=20, error="User name must have between {min} and {max} characters.")
    ]

    username = fields.String(required=True, validate=validate.Length(min=5, error="User name must be at least {min} characters."))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=password_validator)


class UserResponseSchema(Schema):
    """User response schema"""
    id = fields.String()
    username = fields.String()
    email = fields.Email()


class Status(enum.Enum):
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"

    def __str__(self):
        return self.value