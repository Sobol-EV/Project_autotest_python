import pytest


class BaseApi:

    authorize = True

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, api_client_user_block, api_client_user_unlock):
        self.api_client_user_block = api_client_user_block
        self.api_client_user_unlock = api_client_user_unlock

        if self.authorize:
            self.api_client_user_block.authorize()
            self.api_client_user_unlock.authorize()

