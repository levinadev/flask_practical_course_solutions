# Запуск из корня репозитория
# flask --app 04_request_and_response/01_request_object/step_11.py run --debug

"""
Урок 4.1 "Объект request", шаг 11

Создайте приложение `app` с маршрутом `/api/total`, который принимает POST-запрос с JSON вида
`{"prices": [100, 250, 40]}`. Ответ это сумма цен в виде строки, например `390`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    POST /api/total {"prices": [100, 250, 40]}

Пример вывода:

    200 390
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.post("/api/total")
def total():
    data = request.get_json()
    return str(sum(data["prices"]))
