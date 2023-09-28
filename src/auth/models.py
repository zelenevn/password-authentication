from datetime import datetime
from sqlalchemy import Column, Integer, DATE, ForeignKey, Float, VARCHAR

from src.database import Base


class User(Base):
    __tablename__ = 'user'

    username = Column(VARCHAR(16), primary_key=True)
    registered_at = Column(DATE, nullable=False, default=datetime.now().isoformat())
    hashed_password = Column(VARCHAR(32), nullable=False)
    mean = Column(Float, default=None)
    notice_number = Column(Integer, nullable=False, default=0)
    success_enter = Column(Integer, nullable=False, default=0)
    fail_enter = Column(Integer, nullable=False, default=0)


# alembic init migrations
# затем настройка .env, конфига, env.py, а после
# alembic revision --autogenerate -m "Database creation"
# alembic upgrade head
