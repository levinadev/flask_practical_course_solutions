# Запуск из корня репозитория
# flask --app 04_request_and_response/01_request_object/step_08.py run --debug

"""
Урок 4.1 "Объект request", шаг 8

Создайте приложение `app` с маршрутом `/register`, который принимает POST-запросы с полями формы
`name` и `city`. Ответ `<name> из города <city> зарегистрирован`. Если поле `city` не заполнено,
используйте вместо него `неизвестно`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    POST /register name=Анна&city=Казань

Пример вывода:

    200 Анна из города Казань зарегистрирован
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.post("/register")
def register():
    name = request.form.get("name", "")
    city = request.form.get("city") or "неизвестно"
    return f"{name} из города {city} зарегистрирован"
