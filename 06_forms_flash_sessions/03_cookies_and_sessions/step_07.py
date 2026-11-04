# Запуск из корня репозитория
# flask --app 06_forms_flash_sessions/03_cookies_and_sessions/step_07.py run --debug

"""
Урок 6.3 "Cookies и сессии", шаг 7

Запомните выбор языка интерфейса в cookie. Напишите маршруты из таблицы.

Запрос | Что делает
`GET /lang/<code>` | сохраняет `code` в cookie `lang` и перенаправляет на главную (через `url_for`)
`GET /` | отвечает `Привет!`, если в cookie `lang` записано `ru` или cookie нет, `Hello!` для `en` и
`Hola!` для `es`

Для любого другого значения языка главная должна отвечать `Привет!`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Запросы внутри одного теста выполняются одним клиентом, поэтому cookies и сессия сохраняются между
ними.

Пример ввода:

    GET /

Пример вывода:

    200 Привет!
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import make_response, Flask, request, redirect, url_for, flash, session, render_template_string

app = Flask(__name__)
app.secret_key = "dev"


# Решение
@app.route("/lang/<code>")
def set_lang(code):
    response = make_response(redirect(url_for("index")))
    response.set_cookie("lang", code)
    return response


@app.route("/")
def index():
    greetings = {"en": "Hello!", "es": "Hola!"}
    return greetings.get(request.cookies.get("lang"), "Привет!")
