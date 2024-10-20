from dotenv import load_dotenv
from hooks.timing_hook import *
# from hooks.screenshot_hook import *


"""Это нужно, чтобы переменные окружения (такие как логины, пароли, api tokens) не хранились в коде, 
а подгружались из файла .env. Это актуально только для локальных прогонов; 
для запуска через CI переменные будут храниться и подтягиваться из git-secrets.
"""
load_dotenv()

pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth'
]

