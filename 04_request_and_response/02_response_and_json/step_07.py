# Запуск из корня репозитория
# flask --app 04_request_and_response/02_response_and_json/step_07.py run --debug

"""
Урок 4.2 "Формирование ответа и JSON", шаг 7

Создайте приложение `app` с маршрутом `/api/tags`, который принимает POST-запрос с JSON `{"tags":
[...]}`. Он должен вернуть JSON-список уникальных тегов в алфавитном порядке и код 201, а также
заголовок `X-Total-Count` с количеством уникальных тегов.

Пример ввода:

    POST /api/tags {"tags": ["python", "flask", "python"]}

Пример вывода:

    201 ["flask", "python"]
    X-Total-Count: 2
"""

# Решение
from flask import Flask, request, make_response

app = Flask(__name__)


@app.post("/api/tags")
def tags():
    unique = sorted(set(request.get_json()["tags"]))
    response = make_response(unique, 201)
    response.headers["X-Total-Count"] = str(len(unique))
    return response
