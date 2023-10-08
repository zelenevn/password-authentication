from sqlalchemy import Column, DATE, VARCHAR, ARRAY, Float, String
from src.database import Base


class User(Base):
    __tablename__ = 'user'

    username = Column(String, primary_key=True)
    registered_at = Column(DATE, nullable=False)
    expired_at = Column(DATE, nullable=False)
    hashed_password = Column(VARCHAR(32), nullable=False)
    mu_intervals = Column(ARRAY(Float), nullable=False)
    dm_intervals = Column(ARRAY(Float), nullable=False)
    mu_holdings_time = Column(ARRAY(Float), nullable=False)
    dm_holdings_time = Column(ARRAY(Float), nullable=False)
