import pytest
import time


# Хук для початку вимірювання часу перед запуском сесії
def pytest_sessionstart(session):
    session.start_time = time.time()


# Хук для завершення вимірювання часу після завершення сесії
def pytest_sessionfinish (session, exitstatus):
    total_time = time.time() - session.start_time
    print(f"\nЗагальний час виконання тестів: {total_time:.2f} секунд")
