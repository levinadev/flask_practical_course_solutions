# Запуск из корня репозитория
# flask --app 05_jinja_templates/02_conditions_loops_filters/step_07.py run --debug

"""
Урок 5.2 "Условия, циклы и фильтры", шаг 7

Маршрут `/cart` передаёт в шаблон `page.html` список товаров `items` (строки) и булеву переменную
`is_member`. Напишите шаблон, который выводит три строки.

- `<p>Товаров: N</p>`, где N это длина списка (фильтр `length`);
- `<p>ТОВАР1, ТОВАР2</p>` с товарами через запятую с пробелом, заглавными буквами (фильтры `join` и
`upper`), только если список не пустой;
- `<p>Скидка 10%</p>`, если `is_member` истинно.

Приложение `app` и маршрут уже созданы в скрытой части кода. Ваша задача записать текст шаблона в
переменную `TEMPLATE` (обычная строка Python в тройных кавычках).

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /cart?items=чай,сахар&member=1

Пример вывода:

    200 <p>Товаров: 2</p><p>ЧАЙ, САХАР</p><p>Скидка 10%</p>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

from flask import request


@app.route("/cart")
def cart():
    items = [x for x in request.args.get("items", "").split(",") if x]
    return render_template("page.html", items=items, is_member=request.args.get("member") == "1")


# Решение
TEMPLATE = """
<p>Товаров: {{ items|length }}</p>
{% if items %}<p>{{ items|join(", ")|upper }}</p>{% endif %}
{% if is_member %}<p>Скидка 10%</p>{% endif %}
"""


# Скрытая часть кода на Stepik после решения, без неё приложение не запустится
templates = {}
templates['page.html'] = TEMPLATE
app.jinja_loader = DictLoader(templates)
