# Запуск из корня репозитория
# flask --app 05_jinja_templates/04_static_files/step_04.py run --debug

"""
Урок 5.4 "Статические файлы", шаг 4

Маршрут `/` отрисовывает шаблон `page.html` и передаёт в него имя темы оформления `theme` (например,
`dark`). Напишите шаблон из двух тегов. Это `<link rel="stylesheet" href="...">` со ссылкой на файл
`css/<theme>.css` в папке static и `<img src="..." alt="logo">` со ссылкой на `img/logo.png`. Ссылки
стройте через `url_for`.

Приложение `app` и маршрут уже созданы в скрытой части кода. Ваша задача записать текст шаблона в
переменную `TEMPLATE` (обычная строка Python в тройных кавычках).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /?theme=dark

Пример вывода:

    200 <link rel="stylesheet" href="/static/css/dark.css"><img src="/static/img/logo.png" alt="logo">
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

from flask import request


@app.route("/")
def index():
    return render_template("page.html", theme=request.args.get("theme", "light"))


# Решение
TEMPLATE = """
<link rel="stylesheet" href="{{ url_for('static', filename='css/' + theme + '.css') }}">
<img src="{{ url_for('static', filename='img/logo.png') }}" alt="logo">
"""


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
templates = {}
templates['page.html'] = TEMPLATE
app.jinja_loader = DictLoader(templates)
