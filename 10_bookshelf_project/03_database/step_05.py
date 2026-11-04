# Запуск из корня репозитория
# flask --app 10_bookshelf_project/03_database/step_05.py init-db

"""
Урок 10.3 "База данных", шаг 5

Напишите модуль работы с базой, как в уроке. Нужны функции `get_db()` (соединение в `g`, строки как
`sqlite3.Row`), `close_db(exception=None)`, `init_db()`, команду `init-db` (выводит `База данных
создана.`) и `init_app(app)`.

Отличие от урока одно. Схема уже лежит в строковой переменной `SCHEMA`, поэтому в `init_db()`
выполните `get_db().executescript(SCHEMA)` вместо чтения файла. Путь к базе берите из
`current_app.config["DATABASE"]`.

Как проверяется решение. Система создаёт приложение с временной базой, вызывает `init_app(app)` и
выполняет проверки из входных данных. `init-db` запускает команду, `tables` выводит список таблиц,
`same` проверяет, одно ли соединение возвращает get_db() в пределах контекста, `closed` проверяет,
закрыто ли соединение после выхода из контекста, `rows` проверяет, возвращаются ли строки как
sqlite3.Row.

Пример ввода:

    init-db tables

Пример вывода:


    таблицы: []
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
import sqlite3

import click
from flask import Flask, current_app, g

SCHEMA = """
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
"""


# Решение
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    get_db().executescript(SCHEMA)


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("База данных создана.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# Приложение для запуска команды (на Stepik его создаёт проверка)
import os
import tempfile

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(tempfile.gettempdir(), "bookshelf.sqlite")
init_app(app)
