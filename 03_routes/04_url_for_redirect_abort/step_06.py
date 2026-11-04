# Запуск из корня репозитория
# flask --app 03_routes/04_url_for_redirect_abort/step_06.py run --debug

"""
Урок 3.4 "url_for, redirect и abort", шаг 6

В приложении есть словарь книг `BOOKS`. Создайте маршрут `/book/<int:book_id>`. Если книга есть в
словаре, он возвращает её название, иначе ответ с кодом 404 (используйте `abort`).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /book/1

Пример вывода:

    200 Мастер и Маргарита
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
BOOKS = {1: "Мастер и Маргарита", 2: "Война и мир", 3: "Преступление и наказание", 7: "Мёртвые души"}


# Решение
from flask import Flask, abort

app = Flask(__name__)


@app.route("/book/<int:book_id>")
def book(book_id):
    if book_id not in BOOKS:
        abort(404)
    return BOOKS[book_id]
