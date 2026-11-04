# Запуск из корня репозитория
# flask --app 04_request_and_response/03_error_handling/step_05.py run --debug

"""
Урок 4.3 "Обработка ошибок", шаг 5

Создайте API с маршрутом `/api/divide`. Он читает из адреса целые параметры `a` и `b` и возвращает
JSON `{"result": a // b}`. Если какого-то параметра нет или делитель равен нулю, вызовите
`abort(400)`. Обработчик ошибки 400 должен возвращать JSON `{"error": "bad request"}` с кодом 400.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /api/divide?a=10&b=2

Пример вывода:

    200 {"result": 5}
"""

# Решение
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/api/divide")
def divide():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None or b == 0:
        abort(400)
    return {"result": a // b}


@app.errorhandler(400)
def bad_request(error):
    return {"error": "bad request"}, 400
