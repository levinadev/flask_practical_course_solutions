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

Как проверяется решение. После вашего кода система отправляет к приложению `app` запросы через
тестовый клиент Flask и печатает код и текст ответа. Для перенаправлений вместо текста печатается
адрес. Каждая строка во входных данных теста это один запрос, например `GET /hello`. Пробелы и
переносы строк вокруг HTML-тегов при сравнении не учитываются. Запускать сервер не нужно.

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


# Скрытая часть кода на Stepik после решения, она проверяет решение и печатает результат
@app.route("/")
def index():
    return f"Главная: {g.user['username'] if g.user else 'гость'}"


@app.route("/books/<int:book_id>")
@login_required
def book(book_id):
    return f"Книга {book_id} пользователя {g.user['username']}"


app.register_blueprint(bp)
print("имя функции сохранено:", book.__name__ == "book")
import sys as _sys, json as _json, re as _re
_client = app.test_client()
for _line in _sys.stdin.read().splitlines():
    if not _line.strip():
        continue
    _parts = _line.split(" ", 2)
    _kw = {}
    if len(_parts) == 3:
        if _parts[2].startswith("{"):
            _kw["json"] = _json.loads(_parts[2])
        else:
            _kw["data"] = dict(_x.split("=", 1) for _x in _parts[2].split("&"))
    _r = _client.open(_parts[1], method=_parts[0], **_kw)
    _body = _r.get_data(as_text=True).strip()
    if _r.is_json:
        _body = _json.dumps(_r.get_json(), ensure_ascii=False, sort_keys=True)
    else:  # пробелы и переносы вокруг тегов не важны
        _body = _re.sub(r"\s+", " ", _re.sub(r"\s*(<[^>]+>)\s*", r"\1", _body)).strip()
    if 300 <= _r.status_code < 400:
        _body = "-> " + _r.headers.get("Location", "")
    elif _r.status_code >= 400 and _body.lower().startswith("<!doctype html>"):
        _body = ""
    print(_r.status_code, _body) if _body else print(_r.status_code)
