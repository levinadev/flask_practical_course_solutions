# Запуск из корня репозитория
# flask --app 06_forms_flash_sessions/03_cookies_and_sessions/step_06.py run --debug

"""
Урок 6.3 "Cookies и сессии", шаг 6

Сделайте счётчик просмотров на сессиях. В приложении уже задан секретный ключ. Напишите маршруты из
таблицы.

Запрос | Что делает | Ответ
`GET /` | увеличивает счётчик `views` в сессии на 1 | `Просмотров: N`
`GET /reset` | удаляет счётчик из сессии | `Счётчик сброшен`

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Запросы внутри одного теста выполняются одним клиентом, поэтому cookies и сессия сохраняются между
ними.

Пример ввода:

    GET /

Пример вывода:

    200 Просмотров: 1
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, request, redirect, url_for, flash, session, render_template_string

app = Flask(__name__)
app.secret_key = "dev"


# Решение
@app.route("/")
def index():
    session["views"] = session.get("views", 0) + 1
    return f"Просмотров: {session['views']}"


@app.route("/reset")
def reset():
    session.pop("views", None)
    return "Счётчик сброшен"
