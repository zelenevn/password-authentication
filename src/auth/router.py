from sqlalchemy import select, insert
from src.database import get_session
from src.auth.models import User
from src.utils.hash_code import HashCode


# def identify_user(*, username: int, password: str):
#     session = get_session()
#     try:
#         hashed_password = HashCode(password)
#
#         new_user = User(username=username,
#                         registered_at=hashed_password.creation_date,
#                         hashed_password=hashed_password.hex_value)
#
#         return result.all()
#     finally:
#         session.close()


def register_user(*, username: str, password: str):
    session = get_session()
    try:
        hashed_password = HashCode(password)

        new_user = User(username=username,
                        registered_at=hashed_password.creation_date,
                        hashed_password=hashed_password.hex_value)

        session.add(new_user)
        session.commit()
        return {'status': 'success'}
    finally:
        session.close()
