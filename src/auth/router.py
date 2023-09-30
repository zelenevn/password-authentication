from datetime import datetime, timedelta
import numpy as np
from pydantic import ValidationError
from sqlalchemy import select
from src.database import get_session, engine
from src.auth.models import User
from src.utils.hash_code import HashCode
from src.utils.my_math import average_parameter, euclidean_distance, calculate_confidence_interval


def identify_user(*, username: str, password: str, intervals: list[float], holdings_time: list[float]):
    with engine.connect() as conn:
        query = select(User).where(User.username == username.strip())
        user_obj = conn.execute(query).fetchone()

        if user_obj is None:
            raise ValidationError('User does not exist!')

        user = {'username': str(user_obj[0]),
                'registered_at': user_obj[1],
                'expired_at': user_obj[2],
                'hashed_password': str(user_obj[3]),
                'mu_intervals': list(user_obj[4]),
                'dm_intervals': list(user_obj[5]),
                'mu_holdings_time': list(user_obj[6]),
                'dm_holdings_time': list(user_obj[7])}

        if datetime.date(datetime.today()) >= user['expired_at']:
            raise ValidationError('Login expired!')

        hashed_password = HashCode(s=password, salt=user['expired_at'].strftime('%Y-%m-%d'))
        if user['hashed_password'] != hashed_password.hex_value:
            print(hashed_password.hex_value)
            print(user['hashed_password'])
            raise ValidationError('Invalid password!')

        lower, upper = calculate_confidence_interval(user['dm_intervals'])
        print(lower, upper)
        d = euclidean_distance(intervals, user['mu_intervals'])
        print(d)
        if not (lower <= d <= upper):
            raise ValidationError('Invalid intervals!')

        lower, upper = calculate_confidence_interval(user['dm_holdings_time'])
        print(lower, upper)
        d = euclidean_distance(holdings_time, user['mu_holdings_time'])
        print(d)
        if not (lower <= d <= upper):
            raise ValidationError('Invalid holdings time')

        return user


def register_user(*, username: str, password: str, intervals: list[list[float]], holdings_time: list[list[float]]):
    session = get_session()
    try:
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
        k = 5
        multiply_by_k = lambda X: list(np.array(X) * k)

        dm_intervals = multiply_by_k(dm_intervals)
        dm_holdings_time = multiply_by_k(dm_holdings_time)

        new_user = User(username=username.strip(),
                        registered_at=registered_at.isoformat(),
                        expired_at=expired_at.isoformat(),
                        hashed_password=hashed_password.hex_value,
                        mu_intervals=mu_intervals,
                        dm_intervals=dm_intervals,
                        mu_holdings_time=mu_holdings_time,
                        dm_holdings_time=dm_holdings_time)

        session.add(new_user)
        session.commit()
        return {'status': 'success'}

    finally:
        session.close()
