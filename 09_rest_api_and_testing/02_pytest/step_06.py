# Запуск из корня репозитория
# python -m pytest 09_rest_api_and_testing/02_pytest/step_06.py

"""
Урок 9.2 "Тестирование с pytest", шаг 6

Есть API скидок `GET /discount?price=N`. Для цены от 1000 и выше скидка 10%, ниже скидки нет. Ответ
это JSON `{"price": N, "percent": P, "total": T}`, где `total = price - price * percent // 100`. Для
отсутствующей или отрицательной цены ответ `{"error": "bad price"}` с кодом 400.

Напишите тесты, то есть функции `test_...(client)`, которые принимают тестовый клиент. Система
запустит их на правильной версии приложения и на версиях с ошибками. В них граница скидки
сравнивается неправильно, скидка не начисляется совсем, на неверную цену возвращается код 200.
Хорошие тесты проходят на правильной версии и падают на каждой ошибочной.

Как проверяется решение. Входные данные это названия версий приложения. Для каждой версии система
создаёт приложение, запускает все ваши функции `test_...` и печатает, прошли ли они. Версия
`correct` правильная.

Пример ввода:

    correct

Пример вывода:

    correct - все тесты прошли
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, request


def make_app(variant):
    """Приложение-калькулятор скидок; variant задаёт версию: правильную или с ошибкой."""
    app = Flask(__name__)

    @app.route("/discount")
    def discount():
        price = request.args.get("price", type=int)
        if price is None or price < 0:
            return {"error": "bad price"}, 200 if variant == "no_400" else 400
        if variant == "wrong_border":
            percent = 10 if price > 1000 else 0
        elif variant == "no_discount":
            percent = 0
        else:
            percent = 10 if price >= 1000 else 0
        return {"price": price, "percent": percent, "total": price - price * percent // 100}

    return app


# Решение
def test_no_discount_below_border(client):
    data = client.get("/discount?price=999").get_json()
    assert data == {"price": 999, "percent": 0, "total": 999}


def test_discount_on_border(client):
    data = client.get("/discount?price=1000").get_json()
    assert data == {"price": 1000, "percent": 10, "total": 900}


def test_discount_above_border(client):
    data = client.get("/discount?price=2500").get_json()
    assert data["percent"] == 10 and data["total"] == 2250


def test_bad_price(client):
    response = client.get("/discount?price=-5")
    assert response.status_code == 400
    assert client.get("/discount").status_code == 400


# Фикстура client, чтобы тесты запускались через pytest (на Stepik её заменяет проверка)
import pytest


@pytest.fixture
def client():
    return make_app("correct").test_client()
