# Запуск из корня репозитория
# flask --app 08_app_structure/04_authentication/step_06.py run --debug

"""
Урок 8.4 "Аутентификация", шаг 6

Реализуйте регистрацию и вход. Пользователей храните в уже созданном словаре `USERS`, где ключ это
логин, а значение это хеш пароля. Секретный ключ приложения уже задан.

Запрос | Что делает | Ответ
`POST /register` (username, password) | регистрирует пользователя | `Зарегистрирован` с кодом 201;
если логин занят, `Логин занят` с кодом 409
`POST /login` (username, password) | проверяет пароль, при успехе кладёт логин в `session["user"]` |
перенаправление на `/profile`; при ошибке `Неверный логин или пароль` с кодом 401
`GET /profile` | страница только для вошедших (декоратор `login_required`) | `Профиль <логин>`;
гостя перенаправляет на `/login`
`GET /logout` | очищает сессию | перенаправление на `/login`

Маршрут `GET /login` должен отвечать `Форма входа`.

Запросы внутри одного теста выполняются одним клиентом, поэтому сессия сохраняется между ними.

Пример ввода:

    POST /register username=anna&password=qwerty
    POST /login username=anna&password=qwerty
    GET /profile

Пример вывода:

    201 Зарегистрирован
    302 -> /profile
    200 Профиль anna
    пароли захешированы: True
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import functools
from flask import Flask, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "dev"
USERS = {}


# Решение
def login_required(view):
    @functools.wraps(view)
    def wrapped(**kwargs):
        if "user" not in session:
            return redirect(url_for("login_form"))
        return view(**kwargs)
    return wrapped


@app.post("/register")
def register():
    username = request.form["username"]
    if username in USERS:
        return "Логин занят", 409
    USERS[username] = generate_password_hash(request.form["password"])
    return "Зарегистрирован", 201


@app.get("/login")
def login_form():
    return "Форма входа"


@app.post("/login")
def login():
    username = request.form["username"]
    stored = USERS.get(username)
    if stored is None or not check_password_hash(stored, request.form["password"]):
        return "Неверный логин или пароль", 401
    session.clear()
    session["user"] = username
    return redirect(url_for("profile"))


@app.route("/profile")
@login_required
def profile():
    return f"Профиль {session['user']}"


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_form"))
