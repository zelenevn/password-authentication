from datetime import datetime, timedelta
import numpy as np
from pydantic import ValidationError
from sqlalchemy import select
from src.auth.schema import UserValidator
from src.database import get_session, engine
from src.auth.models import User
from src.utils.hash_code import HashCode
from src.utils.my_math import average_parameter, euclidean_distance, calculate_confidence_interval


def create_user(**kwargs) -> bool:
    try:
        user_validator = UserValidator(**kwargs)
        # Проверяем валидность данных
        user_dict = user_validator.model_dump()
        valid_user_data = {k: v for k, v in user_dict.items() if k in User.__table__.columns}
        # Добавляем пользователя в базу данных
        session = get_session()
        try:
            session.add(User(**valid_user_data))
            session.commit()
            return True
        except Exception as e:
            print(e)
            session.rollback()
            return False
        finally:
            session.close()
    except ValidationError as e:
        print(e)
        return False
    except Exception as e:
        print(e)


def identify_user(**kwargs):
    with engine.connect() as conn:
        query = select(User).where(User.username == str(kwargs.get('username')).strip())
        user_obj = conn.execute(query).fetchone()

        if user_obj is None:
            raise ValueError('User does not exist!')

        user_data = {'username': str(user_obj[0]),
                     'registered_at': user_obj[1],
                     'expired_at': user_obj[2],
                     'hashed_password': str(user_obj[3]),
                     'mu_intervals': list(user_obj[4]),
                     'dm_intervals': list(user_obj[5]),
                     'mu_holdings_time': list(user_obj[6]),
                     'dm_holdings_time': list(user_obj[7])}

        try:
            if datetime.date(datetime.today()) > user_data['expired_at']:
                raise ValueError('Login expired!')

            hashed_password = HashCode(s=kwargs.get('password'), salt=user_data['expired_at'].strftime('%Y-%m-%d'))
            if user_data['hashed_password'] != hashed_password.hex_value:
                raise ValueError('Invalid password!')

            lower, upper = calculate_confidence_interval(user_data['dm_intervals'])
            d = euclidean_distance(kwargs.get('intervals'), user_data['mu_intervals'])
            if not (lower <= d <= upper):
                raise ValueError('Invalid intervals!')

            lower, upper = calculate_confidence_interval(user_data['dm_holdings_time'])
            d = euclidean_distance(kwargs.get('holdings_time'), user_data['mu_holdings_time'])
            if not (lower <= d <= upper):
                raise ValueError('Invalid holdings time')

            return {'status': 'permit'}
        except ValueError as e:
            print(e)
            return {'status': 'refuse'}
        except Exception as e:
            print(e)


def register_user(**kwargs):
    registered_at = datetime.now()
    delta = 1
    expired_at = registered_at + timedelta(days=delta)
    hashed_password = HashCode(s=kwargs.get('password'), salt=expired_at.strftime('%Y-%m-%d'))

    mu_intervals = average_parameter(kwargs.get('intervals'))
    mu_holdings_time = average_parameter(kwargs.get('holdings_time'))

    dm_intervals = []
    for intervals_i in kwargs.get('intervals'):
        dm_intervals.append(euclidean_distance(intervals_i, mu_intervals))

    dm_holdings_time = []
    for holdings_time_i in kwargs.get('holdings_time'):
        dm_holdings_time.append(euclidean_distance(holdings_time_i, mu_holdings_time))

    # коэффициент чувствительности
    # чем больше, тем свободнее можно отклоняться от средних показателей

    user_data = {'username': kwargs.get('username').strip(),
                 'registered_at': registered_at.date(),
                 'expired_at': expired_at.date(),
                 'password': kwargs.get('password'),
                 'alphabet': kwargs.get('alphabet'),
                 'hashed_password': hashed_password.hex_value,
                 'mu_intervals': mu_intervals,
                 'dm_intervals': dm_intervals,
                 'mu_holdings_time': mu_holdings_time,
                 'dm_holdings_time': dm_holdings_time}

    if create_user(**user_data):
        return {'status': 'success'}
    else:
        return {'status': 'fail'}
