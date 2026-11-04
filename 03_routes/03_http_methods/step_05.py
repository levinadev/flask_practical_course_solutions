# Запуск из корня репозитория
# flask --app 03_routes/03_http_methods/step_05.py run --debug

"""
Урок 3.3 "HTTP-методы", шаг 5

Создайте приложение `app` для управления заметкой по адресу `/note`. Используйте отдельные функции и
декораторы `@app.get`, `@app.put` и `@app.delete`. Ответы указаны в таблице.

Запрос | Ответ
`GET /note` | `Заметка`
`PUT /note` | `Заметка обновлена`
`DELETE /note` | `Заметка удалена`

Остальные методы должны получать ответ с кодом 405.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    GET /note

Пример вывода:

    200 Заметка
"""

# Решение
from flask import Flask

app = Flask(__name__)


@app.get("/note")
def get_note():
    return "Заметка"


@app.put("/note")
def update_note():
    return "Заметка обновлена"


@app.delete("/note")
def delete_note():
    return "Заметка удалена"
