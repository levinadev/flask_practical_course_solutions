# Запуск из корня репозитория
# flask --app 05_jinja_templates/01_render_template/step_07.py run --debug

"""
Урок 5.1 "Шаблоны и render_template", шаг 7

Маршрут `/order/<int:qty>` отрисовывает шаблон `page.html` и передаёт в него словарь `product` с
ключами `title` и `price` и число `qty`. Напишите шаблон, который выводит
`<h2>НАЗВАНИЕ</h2><p>Итого: СУММА ₽</p>`, где НАЗВАНИЕ это `title` заглавными буквами (метод
`upper()`), а СУММА это `price`, умноженная на `qty`.

Приложение `app` и маршрут уже созданы в скрытой части кода. Ваша задача записать текст шаблона в
переменную `TEMPLATE` (обычная строка Python в тройных кавычках).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /order/1

Пример вывода:

    200 <h2>ЧАЙНИК</h2><p>Итого: 1490 ₽</p>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

PRODUCT = {"title": "Чайник", "price": 1490}


@app.route("/order/<int:qty>")
def order(qty):
    return render_template("page.html", product=PRODUCT, qty=qty)


# Решение
TEMPLATE = """
<h2>{{ product.title.upper() }}</h2>
<p>Итого: {{ product.price * qty }} ₽</p>
"""


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
templates = {}
templates['page.html'] = TEMPLATE
app.jinja_loader = DictLoader(templates)
