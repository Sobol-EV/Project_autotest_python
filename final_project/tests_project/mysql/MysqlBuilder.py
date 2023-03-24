from mysql.models import TestUsersModel
from generators.registration_data import BuilderRegData


class MysqlBuilder:

    def __init__(self, mysql_client):
        self.client = mysql_client
        self.builder = BuilderRegData()

    def create_new_user(self, access, active):
        user_data = self.builder.build()
        new_user = TestUsersModel(
            name=user_data['name'],
            surname=user_data['surname'],
            middle_name=user_data['middle_name'],
            username=user_data['username'],
            password=user_data['password'],
            email=user_data['email'],
            access=access,
            active=active,
            start_active_time=None
        )
        print(self.client)
        self.client.session.add(new_user)
        self.client.session.commit()

        return {
            "info": new_user,
            "user_data": user_data
        }
