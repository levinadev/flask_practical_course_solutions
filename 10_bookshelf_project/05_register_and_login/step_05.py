# Запуск из корня репозитория
# flask --app 10_bookshelf_project/05_register_and_login/step_05.py run --debug

"""
Урок 10.5 "Регистрация и вход", шаг 5

В скрытой части кода есть приложение, словарь пользователей `USERS`, функция `get_user(user_id)` и
blueprint `bp` с маршрутами `auth.login` и `auth.logout` (для простоты вход выполняется по адресу
`/auth/login?id=1`). Напишите две части кода.

- функцию `load_logged_in_user` с декоратором `@bp.before_app_request`, она кладёт в `g.user`
пользователя по `session["user_id"]` или `None`;
- декоратор `login_required`, он при `g.user` равном `None` перенаправляет на
`url_for("auth.login")`; не забудьте `functools.wraps`.

После вашего кода система объявит главную страницу и защищённую страницу `/books/<id>`, подключит
blueprint, проверит, что имя защищённой функции сохранилось, и выполнит запросы.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /

Пример вывода:

    имя функции сохранено: True
    200 Главная: гость
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import functools

from flask import Flask, Blueprint, g, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "dev"
USERS = {1: {"id": 1, "username": "anna"}, 2: {"id": 2, "username": "ivan"}}


def get_user(user_id):
    return USERS.get(user_id)


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    user_id = request.args.get("id", type=int)
    if user_id in USERS:
        session["user_id"] = user_id
        return "Вход выполнен"
    return "Форма входа"


@bp.route("/logout")
def logout():
    session.clear()
    return "Вы вышли"


# Решение
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    g.user = None if user_id is None else get_user(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
@app.route("/")
def index():
    return f"Главная: {g.user['username'] if g.user else 'гость'}"


@app.route("/books/<int:book_id>")
@login_required
def book(book_id):
    return f"Книга {book_id} пользователя {g.user['username']}"


app.register_blueprint(bp)
