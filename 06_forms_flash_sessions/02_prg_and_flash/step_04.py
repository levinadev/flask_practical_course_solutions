# Запуск из корня репозитория
# flask --app 06_forms_flash_sessions/02_prg_and_flash/step_04.py run --debug

"""
Урок 6.2 "Post/Redirect/Get и flash-сообщения", шаг 4

Сделайте простой список дел. В приложении уже есть список `TODOS` и шаблон `PAGE` (строка), который
выводит flash-сообщения и список дел. Напишите два маршрута.

- `GET /` отрисовывает `PAGE` функцией `render_template_string(PAGE, todos=TODOS)`;
- `POST /add` читает поле формы `title`. Если оно пустое, делает flash `Пустая задача`, иначе
добавляет задачу в `TODOS` и делает flash `Задача добавлена`. В обоих случаях идёт перенаправление
на главную через `url_for`.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

В одном тесте может быть несколько запросов подряд. Они выполняются одним и тем же клиентом, поэтому
сессия и flash-сообщения сохраняются между ними.

Пример ввода:

    POST /add title=Купить хлеб
    GET /

Пример вывода:

    302 -> /
    200 <p>Задача добавлена</p><ul><li>Купить хлеб</li></ul>
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
from flask import Flask, request, redirect, url_for, flash, session, render_template_string

app = Flask(__name__)
app.secret_key = "dev"

TODOS = []
PAGE = """{% for m in get_flashed_messages() %}<p>{{ m }}</p>{% endfor %}<ul>{% for t in todos %}<li>{{ t }}</li>{% endfor %}</ul>"""


# Решение
@app.get("/")
def index():
    return render_template_string(PAGE, todos=TODOS)


@app.post("/add")
def add():
    title = request.form.get("title", "").strip()
    if not title:
        flash("Пустая задача")
    else:
        TODOS.append(title)
        flash("Задача добавлена")
    return redirect(url_for("index"))
