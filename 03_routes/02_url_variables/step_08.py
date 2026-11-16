# Запуск из корня репозитория
# flask --app 03_routes/02_url_variables/step_08.py run --debug

"""
Урок 3.2 "Переменные в адресе", шаг 8

Создайте приложение `app`. По адресу `/hello/<name>` оно должно отвечать текстом `Привет, <name>!`,
где вместо `<name>` стоит имя из адреса. Не забудьте экранировать имя функцией `escape` из модуля
`markupsafe`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /hello/anna

Пример вывода:

    200 Привет, anna!
"""

# Решение
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return f"Привет, {escape(name)}!"
