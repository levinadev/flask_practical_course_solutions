"""
Урок 10.8 "Страницы ошибок и тесты", шаг 5

Напишите тесты к упрощённой версии "Книжной полки". В скрытой части есть функция `make_app(variant)`
и помощник `login(client, username="anna", password="secret1")`. Пользователи это `anna` (пароль
`secret1`, книги 1 и 2) и `ivan` (пароль `secret2`, книга 3). Маршруты указаны в таблице.

Запрос | Правильное поведение
`POST /auth/login` | вход; при успехе перенаправление
`POST /books/<id>/delete` | гостя перенаправляет на `/auth/login`; чужую книгу не удаляет, код 403;
свою удаляет и перенаправляет на `/`
`GET /api/stats` | JSON со статистикой только по книгам вошедшего пользователя; гостю код 401

Напишите функции `test_...(client)`. Система запустит их на правильной версии (`correct`) и на
версиях с ошибками. Это удаление без входа (`no_login_required`), удаление чужих книг
(`no_owner_check`), статистика по всем пользователям (`stats_all_users`). Тесты должны проходить на
правильной версии и находить каждую ошибку.

Как проверяется решение. Входные данные это названия версий приложения. Для каждой система запускает
ваши тесты (каждый на свежем приложении) и печатает, прошли ли они.

Пример ввода:

    correct

Пример вывода:

    correct - все тесты прошли
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, request, session, abort

BOOKS = {1: {"owner": "anna", "status": "done"}, 2: {"owner": "anna", "status": "reading"}, 3: {"owner": "ivan", "status": "want"}}
PASSWORDS = {"anna": "secret1", "ivan": "secret2"}


def make_app(variant):
    """Упрощённая "Книжная полка"; variant — правильная версия или версия с ошибкой."""
    app = Flask(__name__)
    app.secret_key = "test"
    books = {k: dict(v) for k, v in BOOKS.items()}

    @app.post("/auth/login")
    def login():
        name = request.form.get("username")
        if PASSWORDS.get(name) != request.form.get("password"):
            return "Неверное имя пользователя или пароль.", 200
        session["user"] = name
        return "", 302, {"Location": "/"}

    @app.post("/books/<int:book_id>/delete")
    def delete(book_id):
        user = session.get("user")
        if user is None and variant != "no_login_required":
            return "", 302, {"Location": "/auth/login"}
        if book_id not in books:
            abort(404)
        if books[book_id]["owner"] != user and variant != "no_owner_check":
            abort(403)
        del books[book_id]
        return "", 302, {"Location": "/"}

    @app.get("/api/stats")
    def stats():
        user = session.get("user")
        if user is None:
            return {"error": "Требуется вход"}, 401
        own = [b for b in books.values() if variant == "stats_all_users" or b["owner"] == user]
        counts = {s: sum(b["status"] == s for b in own) for s in ("want", "reading", "done")}
        return {"total": len(own), **counts}

    return app


def login(client, username="anna", password="secret1"):
    return client.post("/auth/login", data={"username": username, "password": password})


# Решение
def test_guest_cannot_delete(client):
    response = client.post("/books/1/delete")
    assert response.headers["Location"] == "/auth/login"


def test_cannot_delete_other_users_book(client):
    login(client)
    assert client.post("/books/3/delete").status_code == 403


def test_delete_own_book(client):
    login(client)
    assert client.post("/books/1/delete").headers["Location"] == "/"


def test_stats_only_own_books(client):
    login(client)
    assert client.get("/api/stats").get_json() == {"total": 2, "want": 0, "reading": 1, "done": 1}


# Скрытая часть кода на Stepik после решения, она проверяет решение и печатает результат
import sys as _sys, traceback as _tb
_tests = [(_n, _f) for _n, _f in list(globals().items()) if _n.startswith("test_") and callable(_f)]
for _variant in _sys.stdin.read().split():
    _failed = 0
    for _name, _func in _tests:
        try:
            _func(make_app(_variant).test_client())
        except AssertionError:
            _failed += 1
        except Exception:
            _failed += 1
    print(_variant, "-", "все тесты прошли" if _tests and not _failed else "тесты нашли ошибку")
