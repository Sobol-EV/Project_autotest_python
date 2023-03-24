import allure
import pytest
from urls import LOCAL_BASE_URL, DOCKER_BASE_URL


@pytest.fixture(scope='session')
@allure.step("Creating a Selenium Assembly.")
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    local_url = LOCAL_BASE_URL if request.config.getoption('--local') else None
    if local_url:
        url = local_url
    if request.config.getoption('--selenoid'):
        vnc = True if request.config.getoption('--vnc') else False
        selenoid = 'http://selenoid:4444/wd/hub'
    else:
        selenoid = None
        vnc = False
    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'local_url': local_url
    }

