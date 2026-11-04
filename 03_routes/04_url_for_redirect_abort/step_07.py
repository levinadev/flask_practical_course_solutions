# Запуск из корня репозитория
# flask --app 03_routes/04_url_for_redirect_abort/step_07.py run --debug

"""
Урок 3.4 "url_for, redirect и abort", шаг 7

Сайт переехал на новые адреса. Создайте приложение `app` с такими маршрутами.

- функция `profile` по адресу `/user/<name>` отвечает текстом `Профиль <name>`;
- старый адрес `/u/<name>` перенаправляет на профиль, адрес стройте через `redirect(url_for(...))`;
- адрес `/me` перенаправляет на профиль пользователя `guest`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /user/anna

Пример вывода:

    200 Профиль anna
"""

# Решение
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/user/<name>")
def profile(name):
    return f"Профиль {name}"


@app.route("/u/<name>")
def old_profile(name):
    return redirect(url_for("profile", name=name))


@app.route("/me")
def me():
    return redirect(url_for("profile", name="guest"))
