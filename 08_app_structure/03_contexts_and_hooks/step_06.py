# Запуск из корня репозитория
# flask --app 08_app_structure/03_contexts_and_hooks/step_06.py run --debug

"""
Урок 8.3 "Контексты и хуки запроса", шаг 6

Сделайте приложение `app` с "режимом обслуживания". Функция с декоратором `@app.before_request`
сохраняет в `g.user` имя из параметра адреса `user` (по умолчанию `гость`). Если в настройке
`app.config["MAINTENANCE"]` записано `True` и пользователь не `admin`, она сразу возвращает ответ
`Сайт на обслуживании` с кодом 503.

Маршрут `/` отвечает `Привет, <g.user>!`, а `/maintenance/on` включает режим обслуживания (меняет
настройку) и отвечает `Включено`. Изначально `MAINTENANCE` = `False`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /

Пример вывода:

    200 Привет, гость!
"""

# Решение
from flask import Flask, g, request

app = Flask(__name__)
app.config["MAINTENANCE"] = False


@app.before_request
def load_user():
    g.user = request.args.get("user", "гость")
    if app.config["MAINTENANCE"] and g.user != "admin":
        return "Сайт на обслуживании", 503


@app.route("/")
def index():
    return f"Привет, {g.user}!"


@app.route("/maintenance/on")
def maintenance_on():
    app.config["MAINTENANCE"] = True
    return "Включено"
