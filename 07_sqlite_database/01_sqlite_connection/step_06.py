# Запуск из корня репозитория
# flask --app 07_sqlite_database/01_sqlite_connection/step_06.py run --debug

"""
Урок 7.1 "SQLite и соединение с базой", шаг 6

В скрытой части кода создано приложение `app`, а в переменной `DATABASE` лежит путь к файлу базы с
таблицей `books` (поля `id`, `title`, `author`, `year`). Напишите функцию `get_db()`, которая хранит
соединение в `g`, функцию `close_db` с декоратором `@app.teardown_appcontext` и маршрут
`/books/count`, который отвечает `Книг в базе: N`. Дополнительно сделайте маршрут `/authors/count`,
он отвечает `Авторов: N`, где N это число различных авторов.

Пример ввода:

    GET /books/count

Пример вывода:

    200 Книг в базе: 6
    teardown: True
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import os, sqlite3, tempfile
from flask import Flask, g

app = Flask(__name__)
DATABASE = os.path.join(tempfile.mkdtemp(), "books.db")
_c = sqlite3.connect(DATABASE)
_c.executescript("""CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, year INTEGER);
INSERT INTO books (title, author, year) VALUES
  ('Мастер и Маргарита', 'Булгаков', 1967),
  ('Собачье сердце', 'Булгаков', 1987),
  ('Преступление и наказание', 'Достоевский', 1866),
  ('Идиот', 'Достоевский', 1869),
  ('Пикник на обочине', 'Стругацкие', 1972),
  ('Трудно быть богом', 'Стругацкие', 1964);""")
_c.close()


# Решение
import sqlite3
from flask import g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/books/count")
def count_books():
    n = get_db().execute("SELECT COUNT(*) FROM books").fetchone()[0]
    return f"Книг в базе: {n}"


@app.route("/authors/count")
def count_authors():
    n = get_db().execute("SELECT COUNT(DISTINCT author) FROM books").fetchone()[0]
    return f"Авторов: {n}"
