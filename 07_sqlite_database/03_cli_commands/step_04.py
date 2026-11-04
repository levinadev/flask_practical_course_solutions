# Запуск из корня репозитория
# flask --app 07_sqlite_database/03_cli_commands/step_04.py count-books
# flask --app 07_sqlite_database/03_cli_commands/step_04.py add-book "Дюна" Герберт

"""
Урок 7.3 "Команды командной строки", шаг 4

В скрытой части кода создано приложение `app` и соединение `db` с базой в памяти, в таблице `books`
уже есть 6 книг. Добавьте две команды.

Команда | Что делает и выводит
`flask count-books` | выводит `Книг: N`
`flask add-book НАЗВАНИЕ АВТОР` | добавляет книгу (год не указывается) и выводит `Добавлена книга
#id`

Для вывода используйте `click.echo`.

Как проверяется решение. Каждая строка входных данных это команда с аргументами (как после слова
`flask` в терминале). Система выполняет её через тестовый CLI-клиент Flask (`app.test_cli_runner()`)
и печатает вывод команды.

Пример ввода:

    count-books

Пример вывода:

    Книг: 6
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import sqlite3
import click
from flask import Flask

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
@app.cli.command("count-books")
def count_books():
    n = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    click.echo(f"Книг: {n}")


@app.cli.command("add-book")
@click.argument("title")
@click.argument("author")
def add_book(title, author):
    cur = db.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    db.commit()
    click.echo(f"Добавлена книга #{cur.lastrowid}")
