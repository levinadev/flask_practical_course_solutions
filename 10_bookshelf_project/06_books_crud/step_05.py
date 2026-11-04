"""
Урок 10.6 "Книги, создание, изменение, удаление", шаг 5

Напишите две функции из `books.py`.

- `get_book(book_id, check_owner=True)` достаёт книгу из таблицы `book` через `get_db()`;
`abort(404)`, если её нет; `abort(403)`, если `check_owner` истинно, а `book["user_id"]` не
совпадает с `g.user["id"]`;
- `read_form()` возвращает пару `(data, errors)`, это словарь с ключами `title`, `author` (без
пробелов по краям), `status` (по умолчанию `want`), `rating` (целое число или `None`), `note` (без
пробелов по краям) и список ошибок в таком порядке, `Укажите название книги.`, `Укажите автора.`,
`Неизвестный статус.`, `Оценка должна быть от 1 до 5.`

В скрытой части уже есть приложение, `get_db()`, словарь `STATUSES` и `g.user` (пользователь
задаётся параметром `?as=id`). После вашего кода система объявит маршруты `/book/<id>`,
`/public/<id>` (без проверки владельца) и `POST /validate`, который выводит ошибки через `; ` или
разобранные данные.

Как проверяется решение. После вашего кода система отправляет к приложению `app` запросы через
тестовый клиент Flask и печатает код и текст ответа. Для перенаправлений вместо текста печатается
адрес. Каждая строка во входных данных теста это один запрос, например `GET /hello`. Пробелы и
переносы строк вокруг HTML-тегов при сравнении не учитываются. Запускать сервер не нужно.

Пример ввода:

    GET /book/1?as=1

Пример вывода:

    200 Мастер и Маргарита
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import sqlite3

from flask import Flask, g, request, abort

app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.row_factory = sqlite3.Row
db.executescript("""
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'want' CHECK (status IN ('want', 'reading', 'done')),
  rating INTEGER CHECK (rating BETWEEN 1 AND 5),
  note TEXT NOT NULL DEFAULT '',
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
INSERT INTO user (username, password) VALUES ('anna', 'x'), ('ivan', 'y');
INSERT INTO book (user_id, title, author, status, rating) VALUES
  (1, 'Мастер и Маргарита', 'Булгаков', 'done', 5),
  (1, 'Дюна', 'Герберт', 'reading', NULL),
  (2, 'Идиот', 'Достоевский', 'want', NULL);
""")
STATUSES = {"want": "Хочу прочитать", "reading": "Читаю", "done": "Прочитано"}


def get_db():
    return db


@app.before_request
def load_user():
    user_id = request.args.get("as", type=int)
    g.user = None if user_id is None else {"id": user_id}


# Решение
def get_book(book_id, check_owner=True):
    book = get_db().execute("SELECT * FROM book WHERE id = ?", (book_id,)).fetchone()
    if book is None:
        abort(404)
    if check_owner and book["user_id"] != g.user["id"]:
        abort(403)
    return book


def read_form():
    data = {
        "title": request.form.get("title", "").strip(),
        "author": request.form.get("author", "").strip(),
        "status": request.form.get("status", "want"),
        "rating": request.form.get("rating", type=int),
        "note": request.form.get("note", "").strip(),
    }
    errors = []
    if not data["title"]:
        errors.append("Укажите название книги.")
    if not data["author"]:
        errors.append("Укажите автора.")
    if data["status"] not in STATUSES:
        errors.append("Неизвестный статус.")
    if data["rating"] is not None and not 1 <= data["rating"] <= 5:
        errors.append("Оценка должна быть от 1 до 5.")
    return data, errors


# Скрытая часть кода на Stepik после решения, она проверяет решение и печатает результат
@app.route("/book/<int:book_id>")
def show(book_id):
    return get_book(book_id)["title"]


@app.route("/public/<int:book_id>")
def show_public(book_id):
    return get_book(book_id, check_owner=False)["title"]


@app.post("/validate")
def validate():
    data, errors = read_form()
    return "; ".join(errors) if errors else f"ok: {data['title']} / {data['author']} / {data['status']} / {data['rating']} / {data['note']!r}"
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
