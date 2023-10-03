from datetime import datetime, timedelta
import numpy as np
from pydantic import ValidationError
from sqlalchemy import select
from src.auth.schema import UserValidator
from src.database import get_session, engine
from src.auth.models import User
from src.utils.hash_code import HashCode
from src.utils.my_math import average_parameter, euclidean_distance, calculate_confidence_interval


def create_user(user_data: UserValidator):
    # Проверяем валидность данных
    user_dict = user_data.dict()
    user_dict = {k: v for k, v in user_dict.items() if k in User.__table__.columns}
    # Добавляем пользователя в базу данных
    with get_session() as session:
        session.add(User(**user_dict))
        session.commit()
        return True


def identify_user(*, username: str, password: str, intervals: list[float], holdings_time: list[float]):
    with engine.connect() as conn:
        query = select(User).where(User.username == username.strip())
        user_obj = conn.execute(query).fetchone()

        if user_obj is None:
            raise ValueError('User does not exist!')

        user = {'username': str(user_obj[0]),
                'registered_at': user_obj[1],
                'expired_at': user_obj[2],
                'hashed_password': str(user_obj[3]),
                'mu_intervals': list(user_obj[4]),
                'dm_intervals': list(user_obj[5]),
                'mu_holdings_time': list(user_obj[6]),
                'dm_holdings_time': list(user_obj[7])}

        if datetime.date(datetime.today()) >= user['expired_at']:
            raise ValueError('Login expired!')

        hashed_password = HashCode(s=password, salt=user['expired_at'].strftime('%Y-%m-%d'))
        if user['hashed_password'] != hashed_password.hex_value:
            raise ValueError('Invalid password!')

        lower, upper = calculate_confidence_interval(user['dm_intervals'])
        d = euclidean_distance(intervals, user['mu_intervals'])
        if not (lower <= d <= upper):
            raise ValueError('Invalid intervals!')

        lower, upper = calculate_confidence_interval(user['dm_holdings_time'])
        d = euclidean_distance(holdings_time, user['mu_holdings_time'])
        if not (lower <= d <= upper):
            raise ValueError('Invalid holdings time')

        return {'result': user}


def register_user(*, username: str, password: str, alphabet: str, intervals: list[list[float]],
                  holdings_time: list[list[float]]):
    registered_at = datetime.now()
    delta = 1
    expired_at = registered_at + timedelta(days=delta)
    hashed_password = HashCode(s=password, salt=expired_at.strftime('%Y-%m-%d'))

    mu_intervals = average_parameter(intervals)
    mu_holdings_time = average_parameter(holdings_time)

    dm_intervals = []
    for intervals_i in intervals:
        dm_intervals.append(euclidean_distance(intervals_i, mu_intervals))

    dm_holdings_time = []
    for holdings_time_i in holdings_time:
        dm_holdings_time.append(euclidean_distance(holdings_time_i, mu_holdings_time))

    # коэффициент чувствительности
    # чем больше, тем свободнее можно отклоняться от средних показателей
    k = 2.5
    multiply_by_k = lambda X: list(np.array(X) * k)

    dm_intervals = multiply_by_k(dm_intervals)
    dm_holdings_time = multiply_by_k(dm_holdings_time)

    try:
        user_data = UserValidator(username=username.strip(),
                                  registered_at=registered_at.isoformat(),
                                  expired_at=expired_at.isoformat(),
                                  password=password,
                                  alphabet=alphabet,
                                  hashed_password=hashed_password.hex_value,
                                  mu_intervals=mu_intervals,
                                  dm_intervals=dm_intervals,
                                  mu_holdings_time=mu_holdings_time,
                                  dm_holdings_time=dm_holdings_time)
        if create_user(user_data):
            return {'status': 'success'}
        else:
            return {'stasus': 'fail'}
    except ValidationError as e:
        print(e)
    except Exception as e:
        print(e)
