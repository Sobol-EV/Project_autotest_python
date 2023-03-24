from urllib.parse import urljoin
import requests
import json
import os
import allure

import api.error_classes as error_cls


class ApiClient:

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.base_login_url = urljoin(base_url, "/login")
        self.user = user
        self.password = password

        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None,
                 expected_status=200, jsonify=False, params=None, files=None):

        url = urljoin(self.base_url, location)
        response = self.session.request(method=method, url=url, headers=headers,
                                        data=data, params=params, files=files)

        if response.status_code != expected_status:
            raise error_cls.ResponseStatusCodeException(
                f'Got {response.status_code} {response.reason} for URL "{url}"'
            )

        if jsonify:
            json_response = response.json()
            if json_response.get('error', False):
                error = json_response['error']
                raise error_cls.RespondErrorException(
                    f'Request {url} returned error {error["message"]}!'
                )

            return json_response

        return response

    @allure.step(f"Authorization ")
    def authorize(self):
        url_auth = urljoin(self.base_login_url, '/login')
        with allure.step(f"URL:{url_auth} - {self.user} - {self.password}"):
            pass
        headers = {
            'Referer': self.base_url
        }
        data = {
            "username": self.user,
            "password": self.password,
            "submit": "Login"
        }
        response = self.session.post(url=url_auth, data=data, headers=headers)

        return response

    @allure.step("User creation")
    def post_create_user(self, payload, expected_status):
        location = '/api/user'
        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="POST", location=location,
                             headers=headers, data=payload, expected_status=expected_status)

    @allure.step("Deleting a user")
    def delete_user(self, username):
        location = f'/api/user/{username}'
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="DELETE", location=location, headers=headers, expected_status=204)

    @allure.step("Change password for {username} on {payload['password']}")
    def put_change_password_user(self, payload, username):
        location = f'/api/user/{username}/change-password'
        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="PUT", location=location, headers=headers, data=payload)

    @allure.step("User blocking {username}")
    def post_user_block(self, username):
        location = f'/api/user/{username}/block'
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="POST", location=location, headers=headers)

    @allure.step("User unlocking {username}")
    def post_user_unlock(self, username):
        location = f'/api/user/{username}/accept'
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="POST", location=location, headers=headers)

    @allure.step("Checking the status of the application")
    def get_app_status(self):
        location = f'/status'
        headers = {
            'Content-Type': "application/json"
        }

        return self._request(method="GET", location=location, headers=headers)

