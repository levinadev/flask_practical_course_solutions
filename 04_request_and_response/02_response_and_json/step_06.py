# Запуск из корня репозитория
# flask --app 04_request_and_response/02_response_and_json/step_06.py run --debug

"""
Урок 4.2 "Формирование ответа и JSON", шаг 6

Создайте приложение `app` с маршрутом `/api/user/<int:user_id>`. Данные пользователей лежат в
словаре `USERS`. Если пользователь найден, верните его данные как JSON (словарь целиком). Если нет,
верните JSON `{"error": "not found"}` с кодом 404.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /api/user/1

Пример вывода:

    200 {"age": 28, "name": "Анна"}
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
USERS = {1: {"name": "Анна", "age": 28}, 2: {"name": "Иван", "age": 35}, 5: {"name": "Олег", "age": 19}}


# Решение
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/user/<int:user_id>")
def get_user(user_id):
    if user_id not in USERS:
        return jsonify(error="not found"), 404
    return USERS[user_id]
