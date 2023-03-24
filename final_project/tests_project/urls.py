# Url - для работы внутри сети selenoid в Docker
DOCKER_BASE_URL = "http://myapp_proxy:4040"
DOCKER_REGISTRATION_URL = "http://myapp_proxy:4040/reg"
DOCKER_LOGIN_PAGE = "http://myapp_proxy:4040/login"
DOCKER_WELCOME_PAGE = "http://myapp_proxy:4040/welcome/"
DOCKER_INVALID_PAGE = "http://myapp_proxy:4040/invalid_url"

# Url - для локальной работы
LOCAL_BASE_URL = "http://localhost:8083"
LOCAL_REGISTRATION_URL = "http://localhost:8083/reg"
LOCAL_LOGIN_PAGE = "http://localhost:8083/login"
LOCAL_WELCOME_PAGE = "http://localhost:8083/welcome/"
LOCAL_INVALID_PAGE = "http://localhost:8083/invalid_url"

# url - mock - серверов
MOCK_ADD_USER = "http://vk_api:8085/"

