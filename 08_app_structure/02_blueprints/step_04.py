# Запуск из корня репозитория
# flask --app 08_app_structure/02_blueprints/step_04.py run --debug

"""
Урок 8.2 "Blueprints", шаг 4

Создайте два blueprint из таблицы и подключите их к приложению `app`.

Blueprint | Префикс | Маршруты
`books` | `/books` | `/` отвечает `Список книг`; `/<int:book_id>` отвечает `Книга <book_id>`
(функция `detail`)
`admin` | `/admin` | `/` отвечает текстом со ссылкой на книгу №1, построенной через `url_for`, то
есть `Ссылка: /books/1`

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /books/

Пример вывода:

    200 Список книг
"""

# Решение
from flask import Flask, Blueprint, url_for

books = Blueprint("books", __name__, url_prefix="/books")
admin = Blueprint("admin", __name__, url_prefix="/admin")


@books.route("/")
def book_list():
    return "Список книг"


@books.route("/<int:book_id>")
def detail(book_id):
    return f"Книга {book_id}"


@admin.route("/")
def dashboard():
    return f"Ссылка: {url_for('books.detail', book_id=1)}"


app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(admin)
