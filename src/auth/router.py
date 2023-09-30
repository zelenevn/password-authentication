from datetime import datetime, timedelta
from pydantic import ValidationError
from sqlalchemy import select, insert, inspect
from src.database import get_session
from src.auth.models import User
from src.utils.hash_code import HashCode
from src.utils.my_stats import average_parameter, euclidean_distance, calculate_confidence_interval

# дописать функцию
def identify_user(*, username: str, password: str, intervals: list[float], holdings_time: list[float]):
    session = get_session()
    try:
        query = select(User).where(User.username == username)
        result = session.execute(query).fetchone()

        if result:
            columns = result.keys()
            values = result.values()
            user = dict(zip(columns, values))
        else:
            raise ValidationError('User doesn\'t exist!')

        if user.get('hashed_password') != HashCode(password, user.get('expired_at')).hex_value:
            raise ValidationError('Invalid password!')

        return user

    finally:
        session.close()


def register_user(*, username: str, password: str, intervals: list[list[float]], holdings_time: list[list[float]]):
    session = get_session()
    try:
        registered_at = datetime.now()
        delta = 1
        expired_at = datetime.now() + timedelta(days=delta)
        hashed_password = HashCode(password=password, salt=expired_at)

        mu_intervals = average_parameter(intervals)
        mu_holdings_time = average_parameter(holdings_time)

        dm_intervals = []
        for intervals_i in intervals:
            dm_intervals.append(euclidean_distance(intervals_i, mu_intervals))

        dm_holdings_time = []
        for holdings_time_i in holdings_time:
            dm_holdings_time.append(euclidean_distance(holdings_time_i, mu_holdings_time))

        confidence_interval_for_dm_intervals = calculate_confidence_interval(dm_intervals)
        confidence_interval_for_dm_holdings_time = calculate_confidence_interval(dm_holdings_time)

        new_user = User(username=username,
                        registered_at=registered_at.isoformat(),
                        expired_at=expired_at.isoformat(),
                        hashed_password=hashed_password.hex_value,
                        metric_for_intervals=confidence_interval_for_dm_intervals,
                        metric_for_holdings_time=confidence_interval_for_dm_holdings_time)

        session.add(new_user)
        session.commit()
        return {'status': 'success'}

    finally:
        session.close()
