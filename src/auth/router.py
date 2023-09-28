from datetime import datetime, timedelta

from sqlalchemy import select, insert, inspect
from src.database import get_session
from src.auth.models import User
from src.utils.hash_code import HashCode

# Дописать функцию
def identify_user(*, username: int, password: str, intervals: list):
    session = get_session()
    try:
        sub_query = select(User.expired_at, User.mean).where(User.username == username)
        sub_result = session.execute(sub_query)
        dic = sub_result.first()
        print(dic)
        query = select(User).where(User.hashed_password == HashCode(password, dic.get('expired_at')).hex_value and
                                   User.username == username)
        result = session.execute(query)

        return result.all()
    finally:
        session.close()


def register_user(*, username: str, password: str):
    session = get_session()
    try:
        registered_at = datetime.now()
        delta = 1
        expired_at = datetime.now() + timedelta(days=delta)
        hashed_password = HashCode(password, expired_at.isoformat())

        new_user = User(username=username,
                        registered_at=registered_at.isoformat(),
                        expired_at=expired_at.isoformat(),
                        hashed_password=hashed_password.hex_value)

        session.add(new_user)
        session.commit()
        return {'status': 'success'}
    finally:
        session.close()
