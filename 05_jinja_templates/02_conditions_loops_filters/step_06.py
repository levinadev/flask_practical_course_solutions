# Запуск из корня репозитория
# flask --app 05_jinja_templates/02_conditions_loops_filters/step_06.py run --debug

"""
Урок 5.2 "Условия, циклы и фильтры", шаг 6

Маршрут `/books` передаёт в шаблон `page.html` список `books`. Каждая книга это словарь с ключами
`title` и `year`. Напишите шаблон, который выводит маркированный список `<ul>`, где каждый пункт
имеет вид `<li>1. Название (год)</li>` с порядковым номером. Если список пуст, выведите единственный
пункт `<li>Книг пока нет</li>`.

Приложение `app` и маршрут уже созданы в скрытой части кода. Ваша задача записать текст шаблона в
переменную `TEMPLATE` (обычная строка Python в тройных кавычках).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /books?data=[{"title":"Дюна","year":1965}]

Пример вывода:

    200 <ul><li>1. Дюна (1965)</li></ul>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

import json
from flask import request


@app.route("/books")
def books():
    return render_template("page.html", books=json.loads(request.args.get("data", "[]")))


# Решение
TEMPLATE = """
<ul>
{% for book in books %}
  <li>{{ loop.index }}. {{ book.title }} ({{ book.year }})</li>
{% else %}
  <li>Книг пока нет</li>
{% endfor %}
</ul>
"""


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
templates = {}
templates['page.html'] = TEMPLATE
app.jinja_loader = DictLoader(templates)
