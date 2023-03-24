from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, SmallInteger, Date, VARCHAR

Base = declarative_base()


class TestUsersModel(Base):

    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TestUsers: id={self.id}, name={self.name}, surname={self.surname}," \
               f" middle_name={self.middle_name}, username={self.username}, password={self.password}," \
               f"email={self.email}, access={self.access}, active={self.active}," \
               f" start_active_time ={self.start_active_time}>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    surname = Column(VARCHAR(255), nullable=False)
    middle_name = Column(VARCHAR(255))
    username = Column(VARCHAR(16), nullable=False, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), nullable=False, unique=True)
    access = Column(SmallInteger, nullable=False)
    active = Column(SmallInteger, nullable=False)
    start_active_time = Column(Date)

