import datetime

from pydantic import BaseModel, validator, ValidationError


class UserValidator(BaseModel):
    username: str
    registered_at: datetime.date
    expired_at: datetime.date
    password: str
    alphabet: str
    hashed_password: str
    mu_intervals: list[float]
    dm_intervals: list[float]
    mu_holdings_time: list[float]
    dm_holdings_time: list[float]

    @validator('username')
    @classmethod
    def validate_username(cls, value):
        if not value.islower() or len(value.split()) != 1 or not (3 <= len(value) <= 20):
            raise ValidationError('Username Error!')
        return value

    @validator('password')
    @classmethod
    def validate_password(cls, value):
        if len(value) < 6:
            raise ValidationError('The password must be at least 6 characters long!')
        return value

    @validator('alphabet')
    @classmethod
    def validate_alphabet(cls, value):
        if len(value) < 30:
            raise ValidationError('The length of the alphabet is at least 30 characters!')
        return value
