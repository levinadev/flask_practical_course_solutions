# Запуск из корня репозитория
# flask --app 05_jinja_templates/03_template_inheritance/step_05.py run --debug

"""
Урок 5.3 "Наследование шаблонов", шаг 5

В приложении есть базовый шаблон `base.html` с блоками `title` и `content`.

    <!doctype html>
    <html>
    <head>
    <title>{% block title %}Книжная полка{% endblock %}</title>
    </head>
    <body>
    <nav>Меню</nav>
    <main>{% block content %}{% endblock %}</main>
    <footer>© 2026</footer>
    </body>
    </html>

Маршрут `/author/<name>` отрисовывает шаблон `page.html` и передаёт в него `name`. Напишите
`page.html`. Он должен наследовать `base.html`, в блоке `title` выводить `<name>, Книжная полка`
(используйте `super()`), а в блоке `content` выводить `<h1>Книги автора <name></h1>`.

Приложение `app` и маршрут уже созданы в скрытой части кода. Ваша задача записать текст шаблона в
переменную `TEMPLATE` (обычная строка Python в тройных кавычках).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /author/Пушкин

Пример вывода:

    200 <!doctype html><html><head><title>Пушкин, Книжная полка</title></head><body><nav>Меню</nav><main><h1>Книги автора Пушкин</h1></main><footer>© 2026</footer></body></html>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

@app.route("/author/<name>")
def author(name):
    return render_template("page.html", name=name)


# Решение
TEMPLATE = """
{% extends "base.html" %}
{% block title %}{{ name }}, {{ super() }}{% endblock %}
{% block content %}<h1>Книги автора {{ name }}</h1>{% endblock %}
"""


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
templates = {'base.html': '<!doctype html><html><head><title>{% block title %}Книжная полка{% endblock %}</title></head><body><nav>Меню</nav><main>{% block content %}{% endblock %}</main><footer>© 2026</footer></body></html>'}
templates['page.html'] = TEMPLATE
app.jinja_loader = DictLoader(templates)
