import logging
import os
from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine, Column, ForeignKey, Date
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import VARCHAR, Integer, DECIMAL

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


try:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        load_dotenv('.env')
    else:
        raise FileExistsError('Не существует .env файл!')
except Exception as e:
    logging.exception(e)

engine = create_engine('postgresql://{}:{}@localhost:5432/{}'.format(os.getenv('LOGIN'),
                                                                     os.getenv('PASSWORD'),
                                                                     os.getenv('DB_NAME')))

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)


Base = declarative_base()


class IdentifiedUsers(Base):
    __tablename__ = 'identified_users'

    id = Column(VARCHAR(64), primary_key=True)
    creation_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)


class LoginAttempts(Base):
    __tablename__ = 'login_attempts'

    id = Column(VARCHAR(64), ForeignKey('identified_users.id'), primary_key=True, nullable=False)
    successful_attempts = Column(Integer, nullable=False)
    unsuccessful_attempts = Column(Integer, nullable=False)
    metrics = Column(ARRAY(DECIMAL), nullable=False)


Base.metadata.create_all(engine, checkfirst=True)


def insert_values_in_table_login_attempts(id: str,
                                          successful_attempts: int,
                                          unsuccessful_attempts: int,
                                          metrics,
                                          session) -> bool:

    identified_user = session.query(IdentifiedUsers).filter_by(id=id).first()
    new_attempt = LoginAttempts(id=identified_user.id,
                                successful_attempts=successful_attempts,
                                unsuccessful_attempts=unsuccessful_attempts,
                                metrics=metrics)
    session.add(new_attempt)
    logging.info('Запись о попытке входа была успешно добавлена!')
    return True


def insert_values_in_table_authorized_users(id: str, creation_date: str, expiration_date: str, metrics) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = IdentifiedUsers(id=id, creation_date=creation_date, expiration_date=expiration_date)
    session.add(new_user)
    insert_values_in_table_login_attempts(id, 0, 0, metrics, session)
    session.commit()

    logging.info('Пользователь был успешно зарегистрирован!')
    return True
