# Запуск из корня репозитория
# flask --app 04_request_and_response/01_request_object/step_06.py run --debug

"""
Урок 4.1 "Объект request", шаг 6

Создайте приложение `app` с маршрутом `/catalog`. Он читает из адреса номер страницы `page` и
количество товаров на странице `size`, оба целые числа. По умолчанию `page` = 1, `size` = 10. Ответ
это текст `Товары с <start> по <end>`, где start и end это номера первого и последнего товара на
странице (нумерация с 1).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /catalog

Пример вывода:

    200 Товары с 1 по 10
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.route("/catalog")
def catalog():
    page = request.args.get("page", 1, type=int)
    size = request.args.get("size", 10, type=int)
    start = (page - 1) * size + 1
    return f"Товары с {start} по {start + size - 1}"
