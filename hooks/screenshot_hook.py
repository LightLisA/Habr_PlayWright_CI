import pytest
import allure
from playwright.sync_api import Page
import os


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page: Page):
    yield
    # Перевіряємо, чи атрибут rep_call існує, і чи тест завершився з помилкою
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        # Вказуємо шлях до файлу для збереження скріншоту
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        # Створюємо директорію, якщо вона не існує
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        # Зберігаємо скріншот у файл
        page.screenshot(path=screenshot_path, full_page=True)
        # Прикріплюємо файл до Allure звіту
        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name="Скріншот при помилці",
                attachment_type=allure.attachment_type.PNG
            )
