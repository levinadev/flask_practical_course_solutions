# Запуск из корня репозитория
# flask --app 06_forms_flash_sessions/01_html_forms/step_05.py run --debug

"""
Урок 6.1 "HTML-формы", шаг 5

Создайте маршрут `/signup`, который принимает POST-запрос с полями формы `email` и `password` и
проверяет их по порядку.

Условие | Ответ
email пустой или в нём нет символа `@` | `Некорректный email` с кодом 400
пароль короче 8 символов | `Пароль слишком короткий` с кодом 400
всё в порядке | `Аккаунт <email> создан` с кодом 201

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    POST /signup email=anna@mail.ru&password=12345678

Пример вывода:

    201 Аккаунт anna@mail.ru создан
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.post("/signup")
def signup():
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    if "@" not in email:
        return "Некорректный email", 400
    if len(password) < 8:
        return "Пароль слишком короткий", 400
    return f"Аккаунт {email} создан", 201
