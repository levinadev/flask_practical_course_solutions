# Запуск из корня репозитория
# flask --app 08_app_structure/01_app_factory_and_config/step_05.py run --debug

"""
Урок 8.1 "Фабрика приложения и конфигурация", шаг 5

Напишите фабрику `create_app(test_config=None)`. Она создаёт приложение, задаёт настройки по
умолчанию `SITE_NAME="Книжная полка"` и `BOOKS_PER_PAGE=10`, а если передан `test_config`, дополняет
и переопределяет ими настройки. Внутри фабрики объявите маршруты из таблицы.

Адрес | Ответ
`/` | `Добро пожаловать в <SITE_NAME>`
`/per-page` | значение `BOOKS_PER_PAGE` текстом
`/testing` | `yes`, если `app.config["TESTING"]` истинно, иначе `no`

Как проверяется решение. Первая строка входных данных теста это тестовая конфигурация в формате
JSON, которую система передаёт в `create_app(...)` (символ `-` означает вызов `create_app()` без
аргумента). Остальные строки это запросы к созданному приложению. Для каждого печатается код ответа
и текст.

Пример ввода:

    -
    GET /
    GET /per-page
    GET /testing

Пример вывода:

    200 Добро пожаловать в Книжная полка
    200 10
    200 no
"""

# Решение
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SITE_NAME="Книжная полка", BOOKS_PER_PAGE=10)
    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        return f"Добро пожаловать в {app.config['SITE_NAME']}"

    @app.route("/per-page")
    def per_page():
        return str(app.config["BOOKS_PER_PAGE"])

    @app.route("/testing")
    def testing():
        return "yes" if app.config["TESTING"] else "no"

    return app
