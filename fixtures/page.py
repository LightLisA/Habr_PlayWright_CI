import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
import os


def pytest_addoption(parser):
    """Пользовательские опции командной строки

    # Додає опцію для вибору браузера (chrome, remote_chrome або firefox)
    # Додає опцію для вибору режиму headless (True або False)
    # Додає опцію для налаштування розміру вікна браузера (за замовчуванням 1920x1080)
    # Додає опцію для встановлення затримки (slow motion) для симуляції повільніших дій (значення в мілісекундах)
    # Додає опцію для налаштування максимального часу очікування (timeout) для операцій (значення в мілісекундах)
    # Додає опцію для вибору локалі браузера (за замовчуванням 'ru-RU')
    # Коментарований рядок, який можна активувати для налаштування токена для API, наприклад, для інтеграції з Qase

    Пояснення параметрів:

    1. --bn (bn скорочення від "browser name"):
        Вказує, який браузер буде використовуватися для тестування: "chrome", "remote_chrome" або "firefox".
        За замовчуванням встановлено на "chrome".

    2. --h (headless):
        Вказує, чи запустити браузер у headless режимі (тобто без графічного інтерфейсу).
        Значення може бути True або False. За замовчуванням False (тобто з інтерфейсом).

    3. --s (size):
        Визначає розмір вікна браузера. Значення передається у форматі словника з шириною та висотою в пікселях.
        За замовчуванням розмір вікна — 1920x1080.

    4. --slow (slow motion):
        Затримка між діями робота для симуляції повільніших дій (значення у мілісекундах).
        За замовчуванням значення 200 мс.

    5. --t (timeout):
        Максимальний час очікування операції або дії в мілісекундах.
        За замовчуванням значення — 60000 мс (60 секунд).

    6. --l (locale):
        Визначає локаль (мову та регіон) для браузера, наприклад, ru-RU для російської або en-US для англійської.
        За замовчуванням встановлено 'ru-RU'.

    7. Коментарований код:
        У рядку з parser.addini ви можете налаштувати Qase API token через змінну середовища QASE_TOKEN, але цей рядок наразі закоментований.

    pytest --bn=firefox --h=True --s="{'width':1280,'height':720}" --slow=500 --t=120000 --l=en-US
    """
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome, remote_chrome or firefox")
    parser.addoption('--h', action='store', default=False, help='Choose headless: True or False')
    parser.addoption('--s', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width,height')
    parser.addoption('--slow', action='store', default=200, help='Choose slow_mo for robot action')
    parser.addoption('--t', action='store', default=60000, help='Choose timeout')
    parser.addoption('--l', action='store', default='ru-RU', help='Choose locale')
    # parser.addini('qs_to_api_token', default=os.getenv("QASE_TOKEN"), help='Qase app token')


@pytest.fixture(scope='class')
def page(request) -> Page:
    playwright = sync_playwright().start()
    if request.config.getoption("bn") == 'remote_chrome':
        browser = get_remote_chrome(playwright, request)
        context = get_context(browser, request, 'remote')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'firefox':
        browser = get_firefox_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    elif request.config.getoption("bn") == 'chrome':
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright, request)
        context = get_context(browser, request, 'local')
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def get_firefox_browser(playwright, request) -> Browser:
    return playwright.firefox.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
    )


def get_chrome_browser(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=request.config.getoption("h"),
        slow_mo=request.config.getoption("slow"),
        args=['--start-maximized']
    )


def get_remote_chrome(playwright, request) -> Browser:
    return playwright.chromium.launch(
        headless=True,
        slow_mo=request.config.getoption("slow")
    )


def get_context(browser, request, start) -> BrowserContext:
    if start == 'local':
        context = browser.new_context(
            no_viewport=True,
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        # додаємо куки, якщо потрібні
        # context.add_cookies([{'url': 'https://example.com', 'name': 'ab_test', 'value': 'd'}])
        return context

    elif start == 'remote':
        context = browser.new_context(
            viewport=request.config.getoption('s'),
            locale=request.config.getoption('l')
        )
        context.set_default_timeout(
            timeout=request.config.getoption('t')
        )
        # додаємо куки, якщо потрібні
        # context.add_cookies([{'url': 'https://example.com', 'name': 'ab_test', 'value': 'd'}])
        return context


@pytest.fixture(scope="function")
def return_back(browser):
    browser.go_back()
