# Запуск из корня репозитория
# flask --app 10_bookshelf_project/06_books_crud/step_05.py run --debug

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

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

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


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
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
