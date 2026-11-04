# Запуск из корня репозитория
# flask --app 03_routes/02_url_variables/step_08.py run --debug

"""
Урок 3.2 "Переменные в адресе", шаг 8

Создайте приложение `app` для "файлового хранилища". По адресу `/files/<путь>` оно должно отвечать
текстом `Файл: <путь>`. Путь может содержать слеши, например для `/files/docs/2024/report.pdf` ответ
`Файл: docs/2024/report.pdf`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /files/report.pdf

Пример вывода:

    200 Файл: report.pdf
"""

# Решение
from flask import Flask

app = Flask(__name__)


@app.route("/files/<path:filepath>")
def files(filepath):
    return f"Файл: {filepath}"
