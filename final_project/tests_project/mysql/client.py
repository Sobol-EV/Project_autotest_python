import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from mysql.models import Base
from mysql.models import TestUsersModel

class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = 3306
        self.password = password
        # self.host = '127.0.0.1'
        self.host = 'db'
        self.db_name = db_name
        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):

        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        print(url)
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def create_table_test_users(self):
        if not inspect(self.engine).has_table('test_users'):
            Base.metadata.tables['test_users'].create(self.engine)

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def get_created_user(self, **filters):
        self.session.commit()
        res = self.session.query(TestUsersModel).filter_by(**filters)
        res = res.all()
        if res:
            res = res[0]
        return res

    def delete_user(self, **filters):
        self.session.commit()
        self.session.query(TestUsersModel).filter_by(**filters).delete()
        self.session.commit()
