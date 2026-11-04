# Запуск из корня репозитория
# flask --app 05_jinja_templates/01_render_template/step_06.py run --debug

"""
Урок 5.1 "Шаблоны и render_template", шаг 6

Приложение `app` и шаблон `profile.html` уже созданы. Шаблон выводит имя и возраст пользователя из
переменных `name` и `age`. Напишите маршрут `/user/<name>/<int:age>`, который отрисовывает этот
шаблон функцией `render_template`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /user/Анна/28

Пример вывода:

    200 <h1>Анна</h1><p>Возраст: 28</p>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)
app.jinja_loader = DictLoader({"profile.html": "<h1>{{ name }}</h1><p>Возраст: {{ age }}</p>"})


# Решение
@app.route("/user/<name>/<int:age>")
def user(name, age):
    return render_template("profile.html", name=name, age=age)
