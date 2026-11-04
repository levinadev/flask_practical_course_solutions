"""
Урок 10.7 "JSON API", шаг 4

В скрытой части есть приложение с базой книг, `get_db()`, `STATUSES`, `g.user` (задаётся параметром
`?as=id`, без него `None`) и blueprint `bp` с префиксом `/api`. Напишите для него код из таблицы.

Что | Поведение
`@bp.before_request` | если `g.user` равен `None`, ответ `{"error": "Требуется вход"}` с кодом 401
`GET /api/books` | список книг пользователя по возрастанию id, `[{"id": ..., "title": ..., "status":
...}]`; параметр `status` (если он есть в STATUSES) фильтрует книги
`GET /api/stats` | `{"total": N, "want": n1, "reading": n2, "done": n3}` для книг пользователя

После вашего кода система подключит blueprint к приложению.

Пример ввода:

    GET /api/books

Пример вывода:

    401 {"error": "Требуется вход"}
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import sqlite3

from flask import Flask, Blueprint, g, request, abort

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


bp = Blueprint("api", __name__, url_prefix="/api")


# Решение
@bp.before_request
def require_login():
    if g.user is None:
        return {"error": "Требуется вход"}, 401


@bp.get("/books")
def list_books():
    query = "SELECT id, title, status FROM book WHERE user_id = ?"
    params = [g.user["id"]]
    status = request.args.get("status")
    if status in STATUSES:
        query += " AND status = ?"
        params.append(status)
    rows = get_db().execute(query + " ORDER BY id", params).fetchall()
    return [dict(row) for row in rows]


@bp.get("/stats")
def stats():
    counts = {key: 0 for key in STATUSES}
    for row in get_db().execute("SELECT status, COUNT(*) AS n FROM book WHERE user_id = ? GROUP BY status", (g.user["id"],)):
        counts[row["status"]] = row["n"]
    return {"total": sum(counts.values()), **counts}


# Скрытая часть кода на Stepik после решения, она проверяет решение и печатает результат
app.register_blueprint(bp)
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
