# Запуск из корня репозитория
# flask --app 07_sqlite_database/02_crud_and_parameters/step_06.py run --debug

"""
Урок 7.2 "CRUD и параметризованные запросы", шаг 6

В скрытой части кода создано приложение `app` и соединение `db` с базой в памяти. В таблице `books`
есть поля `id`, `title`, `author`, `year`. Напишите маршрут `/books`, который возвращает JSON-список
названий книг. Если в адресе передан параметр `author`, верните только книги этого автора. Книги
должны быть упорядочены по году издания. Используйте параметризованный запрос.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /books

Пример вывода:

    200 ["Преступление и наказание", "Идиот", "Трудно быть богом", "Мастер и Маргарита", "Пикник на обочине", "Собачье сердце"]
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import sqlite3
from flask import Flask, request, abort

app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.row_factory = sqlite3.Row
db.executescript("""CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author TEXT NOT NULL, year INTEGER);
INSERT INTO books (title, author, year) VALUES
  ('Мастер и Маргарита', 'Булгаков', 1967),
  ('Собачье сердце', 'Булгаков', 1987),
  ('Преступление и наказание', 'Достоевский', 1866),
  ('Идиот', 'Достоевский', 1869),
  ('Пикник на обочине', 'Стругацкие', 1972),
  ('Трудно быть богом', 'Стругацкие', 1964);""")


# Решение
@app.route("/books")
def books():
    author = request.args.get("author")
    if author:
        rows = db.execute("SELECT title FROM books WHERE author = ? ORDER BY year", (author,)).fetchall()
    else:
        rows = db.execute("SELECT title FROM books ORDER BY year").fetchall()
    return [row["title"] for row in rows]
