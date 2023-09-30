from datetime import datetime, timedelta
from pydantic import ValidationError
from sqlalchemy import select
from src.database import get_session
from src.auth.models import User
from src.utils.hash_code import HashCode
from src.utils.my_stats import average_parameter, euclidean_distance, calculate_confidence_interval


def identify_user(*, username: str, password: str, intervals: list[float], holdings_time: list[float]):
    session = get_session()
    try:
        query = select(User).where(User.username == username.strip())
        row = session.execute(query).one()
        if row is None:
            raise ValidationError('User doesn\'t exist!')

        if datetime.now().isoformat() < row['expired_at']:
            raise ValidationError('Login expired!')

        if row.get('hashed_password') != HashCode(s=password, salt=row['expired_at']).hex_value:
            raise ValidationError('Invalid password!')

        lower, upper = calculate_confidence_interval(row['reference_for_dm_intervals'])
        if not (lower <= euclidean_distance(intervals, row['reference_for_dm_intervals']) <= upper):
            raise ValidationError('Invalid intervals!')

        lower, upper = calculate_confidence_interval(row['reference_for_dm_holdings_time'])
        if not (lower <= euclidean_distance(holdings_time, row['reference_for_dm_holdings_time']) <= upper):
            raise ValidationError('Invalid holdings time')

        return row

    finally:
        session.close()


def register_user(*, username: str, password: str, intervals: list[list[float]], holdings_time: list[list[float]]):
    session = get_session()
    try:
        registered_at = datetime.now()
        delta = 1
        expired_at = datetime.now() + timedelta(days=delta)
        hashed_password = HashCode(s=password, salt=expired_at)

        mu_intervals = average_parameter(intervals)
        mu_holdings_time = average_parameter(holdings_time)

        dm_intervals = []
        for intervals_i in intervals:
            dm_intervals.append(euclidean_distance(intervals_i, mu_intervals))

        dm_holdings_time = []
        for holdings_time_i in holdings_time:
            dm_holdings_time.append(euclidean_distance(holdings_time_i, mu_holdings_time))

        new_user = User(username=username.strip(),
                        registered_at=registered_at.isoformat(),
                        expired_at=expired_at.isoformat(),
                        hashed_password=hashed_password.hex_value,
                        reference_for_dm_intervals=dm_intervals,
                        reference_for_dm_holdings_time=dm_holdings_time)

        session.add(new_user)
        session.commit()
        return {'status': 'success'}

    finally:
        session.close()
