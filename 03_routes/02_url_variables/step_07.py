# Запуск из корня репозитория
# flask --app 03_routes/02_url_variables/step_07.py run --debug

"""
Урок 3.2 "Переменные в адресе", шаг 7

Создайте приложение `app` с двумя маршрутами.

Адрес | Ответ
`/square/<int:n>` | квадрат числа `n`
`/sum/<int:a>/<int:b>` | сумма чисел `a` и `b`

Ответ это число в виде строки, например для /square/5 ответ `25`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /square/5

Пример вывода:

    200 25
"""

# Решение
from flask import Flask

app = Flask(__name__)


@app.route("/square/<int:n>")
def square(n):
    return str(n * n)


@app.route("/sum/<int:a>/<int:b>")
def total(a, b):
    return str(a + b)
