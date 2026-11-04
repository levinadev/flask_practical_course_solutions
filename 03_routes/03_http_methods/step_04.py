# Запуск из корня репозитория
# flask --app 03_routes/03_http_methods/step_04.py run --debug

"""
Урок 3.3 "HTTP-методы", шаг 4

Создайте приложение `app` с маршрутом `/feedback`, который принимает методы GET и POST. На
GET-запрос он должен отвечать `Оставьте отзыв`, а на POST-запрос `Спасибо за отзыв!`. Используйте
`request.method`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /feedback

Пример вывода:

    200 Оставьте отзыв
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        return "Спасибо за отзыв!"
    return "Оставьте отзыв"
