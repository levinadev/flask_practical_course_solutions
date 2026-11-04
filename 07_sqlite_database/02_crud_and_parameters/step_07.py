# Запуск из корня репозитория
# flask --app 07_sqlite_database/02_crud_and_parameters/step_07.py run --debug

"""
Урок 7.2 "CRUD и параметризованные запросы", шаг 7

Для той же таблицы `books` сделайте маленький JSON API.

Запрос | Что делает | Ответ
`POST /books` | добавляет книгу из JSON {title, author, year} | JSON `{"id": новый id}` с кодом 201;
если нет title или author, то код 400
`GET /books/<id>` | возвращает книгу | JSON {id, title, author, year} или 404
`DELETE /books/<id>` | удаляет книгу | пустой ответ с кодом 204 или 404, если книги нет

Не забудьте `db.commit()` после изменений. Для ошибок используйте `abort(...)`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /books/1

Пример вывода:

    200 {"author": "Булгаков", "id": 1, "title": "Мастер и Маргарита", "year": 1967}
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
@app.post("/books")
def create_book():
    data = request.get_json()
    if not data.get("title") or not data.get("author"):
        abort(400)
    cur = db.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (data["title"], data["author"], data.get("year")))
    db.commit()
    return {"id": cur.lastrowid}, 201


@app.get("/books/<int:book_id>")
def get_book(book_id):
    row = db.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,)).fetchone()
    if row is None:
        abort(404)
    return dict(row)


@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    cur = db.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()
    if cur.rowcount == 0:
        abort(404)
    return "", 204
