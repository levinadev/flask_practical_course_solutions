"""
Урок 3.3 "HTTP-методы", шаг 4

Создайте приложение `app` с маршрутом `/feedback`, который принимает методы GET и POST. На
GET-запрос он должен отвечать `Оставьте отзыв`, а на POST-запрос `Спасибо за отзыв!`. Используйте
`request.method`.

Как проверяется решение. После вашего кода система отправляет к приложению `app` запросы через
тестовый клиент Flask и печатает код и текст ответа. Для перенаправлений вместо текста печатается
адрес. Каждая строка во входных данных теста это один запрос, например `GET /hello`. Пробелы и
переносы строк вокруг HTML-тегов при сравнении не учитываются. Запускать сервер не нужно.

Пример ввода:

    GET /feedback

Пример вывода:

    200 Оставьте отзыв
"""

# Решение
from flask import Flask, request

app = Flask(__name__)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        return "Спасибо за отзыв!"
    return "Оставьте отзыв"


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
