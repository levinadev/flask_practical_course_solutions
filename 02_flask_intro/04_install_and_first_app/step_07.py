# Запуск из корня репозитория
# flask --app 02_flask_intro/04_install_and_first_app/step_07.py run --debug

"""
Урок 2.4 "Установка и первое приложение", шаг 7

Создайте приложение `app` с тремя страницами.

Адрес | Текст ответа
`/` | `Главная`
`/about` | `О нас`
`/contacts` | `Контакты`

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /

Пример вывода:

    200 Главная
"""

# Решение
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Главная"


@app.route("/about")
def about():
    return "О нас"


@app.route("/contacts")
def contacts():
    return "Контакты"
