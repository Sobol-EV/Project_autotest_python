import pytest
import shutil
import sys
import logging
import allure
import os

from ui.fixtures import *
from mysql.fixtures import *
from api.fixtures import *

from mysql.client import MysqlClient
from api.client import ApiClient

from mysql.MysqlBuilder import MysqlBuilder
from urls import LOCAL_BASE_URL, DOCKER_BASE_URL


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default=DOCKER_BASE_URL)
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--local', action='store_true')


def pytest_configure(config):
    mysql_client = MysqlClient(
        user='root',
        password='toor',
        db_name='vkeducation'
    )
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_test_users()
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.mysql_client = mysql_client
    config.base_temp_dir = base_dir


@pytest.fixture(scope='session')
def repo_root_mysql():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@allure.step("Creating a MySQL Client")
@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()


def credentials(block: bool, mysql_client):
    m_builder = MysqlBuilder(mysql_client)
    access = 0 if block else 1
    result = m_builder.create_new_user(access, 0)
    return result["user_data"]["username"], result["user_data"]["password"]


@allure.step("Create a client API for a blocked user")
@pytest.fixture(scope="function")
def api_client_user_block(request, credentials_user_block) -> ApiClient:
    url = request.config.getoption('--url')
    username, password = credentials_user_block
    api_client = ApiClient(url, username, password)
    return api_client


@allure.step("Create a client API for a unlocked user")
@pytest.fixture(scope="function")
def api_client_user_unlock(request, credentials_user_unlock) -> ApiClient:
    url = request.config.getoption('--url')
    username, password = credentials_user_unlock
    api_client = ApiClient(url, username, password)
    return api_client


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


# @pytest.fixture(scope='session')
# def base_temp_dir():
#     if sys.platform.startswith('win'):
#         base_dir = r'C:\tests'
#     else:
#         base_dir = '/tmp/tests'
#     if os.path.exists(base_dir):
#         shutil.rmtree(base_dir)
#     return base_dir

@allure.step("Creating a Path for Files.")
@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(
        request.config.base_temp_dir,
        request._pyfuncitem.nodeid
    )
    test_dir = test_dir.replace('::', '--')
    os.makedirs(test_dir)
    return test_dir

@allure.step("Creating a logger.")
@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
    )
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)
    yield log

    for handler in log.handlers:
        handler.close()


@allure.step('Adding a blocked user to the database')
@pytest.fixture(scope='session')
def credentials_user_block(mysql_client):
    return credentials(True, mysql_client)


@allure.step('Adding a unlocked user to the database')
@pytest.fixture(scope='session')
def credentials_user_unlock(mysql_client):
    return credentials(False, mysql_client)


