import requests
from urls import MOCK_ADD_USER
from urllib.parse import urljoin


class MockClient:

    def add_user(self, username, vk_id):

        requests.post(urljoin(MOCK_ADD_USER, '/vk_id/add_user'),
        json={
            'username': username,
            'vk_id': str(vk_id)
            }
        )
