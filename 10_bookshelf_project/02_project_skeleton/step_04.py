# Запуск из корня репозитория
# flask --app 10_bookshelf_project/02_project_skeleton/step_04.py run --debug

"""
Урок 10.2 "Каркас проекта и фабрика", шаг 4

Напишите фабрику `create_app(test_config=None)` проекта, как в уроке. Нужны папка экземпляра для
конфигурации, `SECRET_KEY` = `dev`, файл `bookshelf.sqlite` в `DATABASE` в папке экземпляра,
переопределение настроек из `test_config`, создание папки экземпляра и маршрут `/hello` с ответом
`Hello, Книжная полка!`.

Как проверяется решение. Входные данные это тестовая конфигурация в формате JSON или `-`, то есть
вызов `create_app()` без аргумента. Система создаёт приложение и печатает его настройки и ответ на
`/hello`.

Пример ввода:

    -

Пример вывода:

    SECRET_KEY: dev
    DATABASE: bookshelf.sqlite
    база в папке экземпляра: True
    папка экземпляра создана: True
    TESTING: False
    /hello: Hello, Книжная полка!
"""

# Решение
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "bookshelf.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route("/hello")
    def hello():
        return "Hello, Книжная полка!"

    return app
