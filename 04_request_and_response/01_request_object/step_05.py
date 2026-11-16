# Запуск из корня репозитория
# flask --app 04_request_and_response/01_request_object/step_05.py run --debug

"""
Урок 4.1 "Объект request", шаг 5

Создайте приложение `app` с маршрутом `/search`. Он читает параметр `q` из адреса и отвечает `Ищем:
<q>`. Если параметра нет или он пустой, ответ должен быть `Пустой запрос`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /search?q=flask

Пример вывода:

    200 Ищем: flask
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    if not q:
        return "Пустой запрос"
    return f"Ищем: {q}"
