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
    print("X-Total-Count:", _r.headers.get("X-Total-Count"))
