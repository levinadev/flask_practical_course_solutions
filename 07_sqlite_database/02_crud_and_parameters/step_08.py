# Запуск из корня репозитория
# flask --app 07_sqlite_database/02_crud_and_parameters/step_08.py run --debug

"""
Урок 7.2 "CRUD и параметризованные запросы", шаг 8

Добавьте к таблице `books` изменение года издания. Маршрут `PATCH /books/<id>` принимает JSON
`{"year": число}` и обновляет книгу. Ответ это JSON `{"updated": id}`. Если книги нет, код 404, если
в JSON нет числа `year`, код 400. Также сделайте `GET /books/<id>/year`, который возвращает год
книги текстом (или 404).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    PATCH /books/1 {"year": 1966}
    GET /books/1/year

Пример вывода:

    200 {"updated": 1}
    200 1966
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
@app.patch("/books/<int:book_id>")
def update_year(book_id):
    year = request.get_json().get("year")
    if not isinstance(year, int):
        abort(400)
    cur = db.execute("UPDATE books SET year = ? WHERE id = ?", (year, book_id))
    db.commit()
    if cur.rowcount == 0:
        abort(404)
    return {"updated": book_id}


@app.get("/books/<int:book_id>/year")
def get_year(book_id):
    row = db.execute("SELECT year FROM books WHERE id = ?", (book_id,)).fetchone()
    if row is None:
        abort(404)
    return str(row["year"])
