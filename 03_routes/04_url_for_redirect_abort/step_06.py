"""
Урок 3.4 "url_for, redirect и abort", шаг 6

В приложении есть словарь книг `BOOKS`. Создайте маршрут `/book/<int:book_id>`. Если книга есть в
словаре, он возвращает её название, иначе ответ с кодом 404 (используйте `abort`).

Как проверяется решение. После вашего кода система отправляет к приложению `app` запросы через
тестовый клиент Flask и печатает код и текст ответа. Для перенаправлений вместо текста печатается
адрес. Каждая строка во входных данных теста это один запрос, например `GET /hello`. Пробелы и
переносы строк вокруг HTML-тегов при сравнении не учитываются. Запускать сервер не нужно.

Пример ввода:

    GET /book/1

Пример вывода:

    200 Мастер и Маргарита
"""

# Скрытая часть кода на Stepik перед решением, её писать не нужно
BOOKS = {1: "Мастер и Маргарита", 2: "Война и мир", 3: "Преступление и наказание", 7: "Мёртвые души"}


# Решение
from flask import Flask, abort

app = Flask(__name__)


@app.route("/book/<int:book_id>")
def book(book_id):
    if book_id not in BOOKS:
        abort(404)
    return BOOKS[book_id]


# Скрытая часть кода на Stepik после решения, она проверяет решение и печатает результат
import sys as _sys, json as _json, re as _re
_client = app.test_client()
for _line in _sys.stdin.read().splitlines():
    if not _line.strip():
        continue
    _parts = _line.split(" ", 2)
    _kw = {}
    if len(_parts) == 3:
        if _parts[2].startswith("{"):
            _kw["json"] = _json.loads(_parts[2])
        else:
            _kw["data"] = dict(_x.split("=", 1) for _x in _parts[2].split("&"))
    _r = _client.open(_parts[1], method=_parts[0], **_kw)
    _body = _r.get_data(as_text=True).strip()
    if _r.is_json:
        _body = _json.dumps(_r.get_json(), ensure_ascii=False, sort_keys=True)
    else:  # пробелы и переносы вокруг тегов не важны
        _body = _re.sub(r"\s+", " ", _re.sub(r"\s*(<[^>]+>)\s*", r"\1", _body)).strip()
    if 300 <= _r.status_code < 400:
        _body = "-> " + _r.headers.get("Location", "")
    elif _r.status_code >= 400 and _body.lower().startswith("<!doctype html>"):
        _body = ""
    print(_r.status_code, _body) if _body else print(_r.status_code)
