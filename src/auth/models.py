from sqlalchemy import Column, DATE, VARCHAR, ARRAY
from src.database import Base


class User(Base):
    __tablename__ = 'user'

    username = Column(VARCHAR(16), primary_key=True)
    registered_at = Column(DATE, nullable=False)
    expired_at = Column(DATE, nullable=False)
    hashed_password = Column(VARCHAR(32), nullable=False)
    metric_for_intervals = Column(ARRAY, nullable=False)
    metric_for_holdings_time = Column(ARRAY, nullable=False)

# alembic revision --autogenerate -m "Database creation"
# alembic upgrade head
