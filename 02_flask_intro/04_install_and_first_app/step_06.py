# Запуск из корня репозитория
# flask --app 02_flask_intro/04_install_and_first_app/step_06.py run --debug

"""
Урок 2.4 "Установка и первое приложение", шаг 6

Создайте Flask-приложение `app` с одной страницей. По адресу `/` оно должно возвращать текст `Hello,
Flask!`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /

Пример вывода:

    200 Hello, Flask!
"""

# Решение
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Flask!"
