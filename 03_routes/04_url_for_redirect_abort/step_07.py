"""
Урок 3.4 "url_for, redirect и abort", шаг 7

Сайт переехал на новые адреса. Создайте приложение `app` с такими маршрутами.

- функция `profile` по адресу `/user/<name>` отвечает текстом `Профиль <name>`;
- старый адрес `/u/<name>` перенаправляет на профиль, адрес стройте через `redirect(url_for(...))`;
- адрес `/me` перенаправляет на профиль пользователя `guest`.

Как проверяется решение. После вашего кода система отправляет к приложению `app` запросы через
тестовый клиент Flask и печатает код и текст ответа. Для перенаправлений вместо текста печатается
адрес. Каждая строка во входных данных теста это один запрос, например `GET /hello`. Пробелы и
переносы строк вокруг HTML-тегов при сравнении не учитываются. Запускать сервер не нужно.

Пример ввода:

    GET /user/anna

Пример вывода:

    200 Профиль anna
"""

# Решение
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/user/<name>")
def profile(name):
    return f"Профиль {name}"


@app.route("/u/<name>")
def old_profile(name):
    return redirect(url_for("profile", name=name))


@app.route("/me")
def me():
    return redirect(url_for("profile", name="guest"))


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
