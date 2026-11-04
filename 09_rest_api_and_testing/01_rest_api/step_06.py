# Запуск из корня репозитория
# flask --app 09_rest_api_and_testing/01_rest_api/step_06.py run --debug

"""
Урок 9.1 "REST API на Flask", шаг 6

Сделайте API списка покупок с ресурсами `/api/items`. Элемент это JSON `{"id": число, "name":
строка, "qty": число}`. Номера выдаются по порядку с 1. Запросы перечислены в таблице.

Запрос | Ответ
`GET /api/items` | 200, список всех элементов
`POST /api/items` (JSON с name и qty) | 201 и созданный элемент; `qty` по умолчанию 1; если `name`
нет или это пустая строка, или `qty` не целое положительное число, то 400 и `{"error": "bad
request"}`
`GET /api/items/<id>` | 200 и элемент или 404 и `{"error": "not found"}`
`PATCH /api/items/<id>` (JSON с qty) | 200 и обновлённый элемент; 404, если нет элемента; 400, если
qty некорректный
`DELETE /api/items/<id>` | 204 или 404

Ошибки 400 и 404 должны возвращаться в JSON, для этого зарегистрируйте обработчики ошибок.

Запускать сервер не нужно, строка `app.run()` в решении не нужна, запросы к приложению отправит
система.

Пример ввода:

    POST /api/items {"name": "Хлеб"}
    GET /api/items

Пример вывода:

    201 {"id": 1, "name": "Хлеб", "qty": 1}
    200 [{"id": 1, "name": "Хлеб", "qty": 1}]
"""

# Решение
from flask import Flask, request, abort

app = Flask(__name__)

ITEMS = {}
next_id = 1


def valid_qty(q):
    return isinstance(q, int) and not isinstance(q, bool) and q > 0


@app.errorhandler(400)
def bad_request(e):
    return {"error": "bad request"}, 400


@app.errorhandler(404)
def not_found(e):
    return {"error": "not found"}, 404


@app.get("/api/items")
def list_items():
    return list(ITEMS.values())


@app.post("/api/items")
def create_item():
    global next_id
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    qty = data.get("qty", 1)
    if not isinstance(name, str) or not name.strip() or not valid_qty(qty):
        abort(400)
    item = {"id": next_id, "name": name, "qty": qty}
    ITEMS[next_id] = item
    next_id += 1
    return item, 201


@app.get("/api/items/<int:item_id>")
def get_item(item_id):
    if item_id not in ITEMS:
        abort(404)
    return ITEMS[item_id]


@app.patch("/api/items/<int:item_id>")
def update_item(item_id):
    if item_id not in ITEMS:
        abort(404)
    qty = (request.get_json(silent=True) or {}).get("qty")
    if not valid_qty(qty):
        abort(400)
    ITEMS[item_id]["qty"] = qty
    return ITEMS[item_id]


@app.delete("/api/items/<int:item_id>")
def delete_item(item_id):
    if ITEMS.pop(item_id, None) is None:
        abort(404)
    return "", 204
