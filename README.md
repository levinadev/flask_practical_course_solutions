# Решения задач курса [Практический курс по Flask](https://stepik.org/course/302580) на Stepik

В репозитории собраны все 45 задач курса на программирование. В файле задачи есть условие, пример из тестов и решение, которое проходит проверку на Stepik. Репозиторий нужен, чтобы после решения задачи можно было сравнить свой код с вариантом автора курса.

## Как пользоваться

1. Сначала решите задачу сами и отправьте решение на Stepik.
2. Найдите файл задачи. Он лежит в папке модуля, внутри неё в папке урока и называется `step_NN.py`, где `NN` означает номер шага в уроке. Ссылки на все файлы есть в содержании ниже.
3. Сравните своё решение с решением из файла. Оно стоит после комментария `# Решение`.

Если задача не получается, не открывайте решение сразу. Перечитайте теорию урока, откройте подсказку под условием на Stepik, запустите приложение у себя и посмотрите, что оно отвечает. Подсмотренное решение почти ничему не учит.

## Что ещё есть в файле

На Stepik к решению добавляется код, которого студент не видит. В файле он тоже есть, поэтому решение запускается так же, как при проверке.

- Код перед решением есть не во всех задачах. Это то, что уже готово в условии, например приложение, словарь с данными или база.
- Код после решения проверяет его. Обычно он отправляет к приложению `app` запросы через тестовый клиент Flask и печатает код и текст ответа, поэтому сервер запускать не нужно.

## Как запустить решение

Нужны Python 3.10 или новее и Flask. Решения проверялись на Flask 3.0.3.

```bash
pip install flask==3.0.3
```

Например, так запускается первая задача.

```bash
python 02_flask_intro/03_install_and_first_app/step_06.py
```

или

```bash
python3 02_flask_intro/03_install_and_first_app/step_06.py
```

После запуска введите данные с клавиатуры, как в примере ввода в начале файла. Обычно каждая строка это один запрос к приложению, например `GET /hello`. После последней строки нажмите `Ctrl+D` (в Windows `Ctrl+Z`, затем `Enter`).

## Содержание

Номер модуля в названии папки совпадает с номером модуля в курсе, а номер урока с номером урока внутри модуля.

### 2. Знакомство с Flask

| Урок | Шаг | Файл |
|---|---|---|
| 2.3 Установка и первое приложение | 6 | [`02_flask_intro/03_install_and_first_app/step_06.py`](02_flask_intro/03_install_and_first_app/step_06.py) |
| 2.3 Установка и первое приложение | 7 | [`02_flask_intro/03_install_and_first_app/step_07.py`](02_flask_intro/03_install_and_first_app/step_07.py) |

### 3. Маршруты

| Урок | Шаг | Файл |
|---|---|---|
| 3.1 Маршруты и функции-представления | 6 | [`03_routes/01_routes_and_views/step_06.py`](03_routes/01_routes_and_views/step_06.py) |
| 3.2 Переменные в адресе | 6 | [`03_routes/02_url_variables/step_06.py`](03_routes/02_url_variables/step_06.py) |
| 3.2 Переменные в адресе | 7 | [`03_routes/02_url_variables/step_07.py`](03_routes/02_url_variables/step_07.py) |
| 3.2 Переменные в адресе | 8 | [`03_routes/02_url_variables/step_08.py`](03_routes/02_url_variables/step_08.py) |
| 3.3 HTTP-методы | 4 | [`03_routes/03_http_methods/step_04.py`](03_routes/03_http_methods/step_04.py) |
| 3.3 HTTP-методы | 5 | [`03_routes/03_http_methods/step_05.py`](03_routes/03_http_methods/step_05.py) |
| 3.4 url_for, redirect и abort | 6 | [`03_routes/04_url_for_redirect_abort/step_06.py`](03_routes/04_url_for_redirect_abort/step_06.py) |
| 3.4 url_for, redirect и abort | 7 | [`03_routes/04_url_for_redirect_abort/step_07.py`](03_routes/04_url_for_redirect_abort/step_07.py) |

### 4. Запрос и ответ

| Урок | Шаг | Файл |
|---|---|---|
| 4.1 Объект request | 6 | [`04_request_and_response/01_request_object/step_06.py`](04_request_and_response/01_request_object/step_06.py) |
| 4.1 Объект request | 7 | [`04_request_and_response/01_request_object/step_07.py`](04_request_and_response/01_request_object/step_07.py) |
| 4.1 Объект request | 8 | [`04_request_and_response/01_request_object/step_08.py`](04_request_and_response/01_request_object/step_08.py) |
| 4.1 Объект request | 9 | [`04_request_and_response/01_request_object/step_09.py`](04_request_and_response/01_request_object/step_09.py) |
| 4.2 Формирование ответа и JSON | 6 | [`04_request_and_response/02_response_and_json/step_06.py`](04_request_and_response/02_response_and_json/step_06.py) |
| 4.2 Формирование ответа и JSON | 7 | [`04_request_and_response/02_response_and_json/step_07.py`](04_request_and_response/02_response_and_json/step_07.py) |
| 4.3 Обработка ошибок | 4 | [`04_request_and_response/03_error_handling/step_04.py`](04_request_and_response/03_error_handling/step_04.py) |
| 4.3 Обработка ошибок | 5 | [`04_request_and_response/03_error_handling/step_05.py`](04_request_and_response/03_error_handling/step_05.py) |

### 5. Шаблоны Jinja

| Урок | Шаг | Файл |
|---|---|---|
| 5.1 Шаблоны и render_template | 6 | [`05_jinja_templates/01_render_template/step_06.py`](05_jinja_templates/01_render_template/step_06.py) |
| 5.1 Шаблоны и render_template | 7 | [`05_jinja_templates/01_render_template/step_07.py`](05_jinja_templates/01_render_template/step_07.py) |
| 5.2 Условия, циклы и фильтры | 6 | [`05_jinja_templates/02_conditions_loops_filters/step_06.py`](05_jinja_templates/02_conditions_loops_filters/step_06.py) |
| 5.2 Условия, циклы и фильтры | 7 | [`05_jinja_templates/02_conditions_loops_filters/step_07.py`](05_jinja_templates/02_conditions_loops_filters/step_07.py) |
| 5.3 Наследование шаблонов | 5 | [`05_jinja_templates/03_template_inheritance/step_05.py`](05_jinja_templates/03_template_inheritance/step_05.py) |
| 5.4 Статические файлы | 4 | [`05_jinja_templates/04_static_files/step_04.py`](05_jinja_templates/04_static_files/step_04.py) |

### 6. Формы, flash-сообщения и сессии

| Урок | Шаг | Файл |
|---|---|---|
| 6.1 HTML-формы | 5 | [`06_forms_flash_sessions/01_html_forms/step_05.py`](06_forms_flash_sessions/01_html_forms/step_05.py) |
| 6.2 Post/Redirect/Get и flash-сообщения | 4 | [`06_forms_flash_sessions/02_prg_and_flash/step_04.py`](06_forms_flash_sessions/02_prg_and_flash/step_04.py) |
| 6.3 Cookies и сессии | 6 | [`06_forms_flash_sessions/03_cookies_and_sessions/step_06.py`](06_forms_flash_sessions/03_cookies_and_sessions/step_06.py) |
| 6.3 Cookies и сессии | 7 | [`06_forms_flash_sessions/03_cookies_and_sessions/step_07.py`](06_forms_flash_sessions/03_cookies_and_sessions/step_07.py) |

### 7. База данных SQLite

| Урок | Шаг | Файл |
|---|---|---|
| 7.1 SQLite и соединение с базой | 6 | [`07_sqlite_database/01_sqlite_connection/step_06.py`](07_sqlite_database/01_sqlite_connection/step_06.py) |
| 7.2 CRUD и параметризованные запросы | 6 | [`07_sqlite_database/02_crud_and_parameters/step_06.py`](07_sqlite_database/02_crud_and_parameters/step_06.py) |
| 7.2 CRUD и параметризованные запросы | 7 | [`07_sqlite_database/02_crud_and_parameters/step_07.py`](07_sqlite_database/02_crud_and_parameters/step_07.py) |
| 7.2 CRUD и параметризованные запросы | 8 | [`07_sqlite_database/02_crud_and_parameters/step_08.py`](07_sqlite_database/02_crud_and_parameters/step_08.py) |
| 7.3 Команды командной строки | 4 | [`07_sqlite_database/03_cli_commands/step_04.py`](07_sqlite_database/03_cli_commands/step_04.py) |

### 8. Структура приложения

| Урок | Шаг | Файл |
|---|---|---|
| 8.1 Фабрика приложения и конфигурация | 5 | [`08_app_structure/01_app_factory_and_config/step_05.py`](08_app_structure/01_app_factory_and_config/step_05.py) |
| 8.2 Blueprints | 4 | [`08_app_structure/02_blueprints/step_04.py`](08_app_structure/02_blueprints/step_04.py) |
| 8.3 Контексты и хуки запроса | 6 | [`08_app_structure/03_contexts_and_hooks/step_06.py`](08_app_structure/03_contexts_and_hooks/step_06.py) |
| 8.4 Аутентификация | 6 | [`08_app_structure/04_authentication/step_06.py`](08_app_structure/04_authentication/step_06.py) |

### 9. REST API и тестирование

| Урок | Шаг | Файл |
|---|---|---|
| 9.1 REST API на Flask | 6 | [`09_rest_api_and_testing/01_rest_api/step_06.py`](09_rest_api_and_testing/01_rest_api/step_06.py) |
| 9.2 Тестирование с pytest | 6 | [`09_rest_api_and_testing/02_pytest/step_06.py`](09_rest_api_and_testing/02_pytest/step_06.py) |

### 10. Финальный проект "Книжная полка"

| Урок | Шаг | Файл |
|---|---|---|
| 10.2 Каркас проекта и фабрика | 4 | [`10_bookshelf_project/02_project_skeleton/step_04.py`](10_bookshelf_project/02_project_skeleton/step_04.py) |
| 10.3 База данных | 5 | [`10_bookshelf_project/03_database/step_05.py`](10_bookshelf_project/03_database/step_05.py) |
| 10.5 Регистрация и вход | 5 | [`10_bookshelf_project/05_register_and_login/step_05.py`](10_bookshelf_project/05_register_and_login/step_05.py) |
| 10.6 Книги, создание, изменение, удаление | 5 | [`10_bookshelf_project/06_books_crud/step_05.py`](10_bookshelf_project/06_books_crud/step_05.py) |
| 10.7 JSON API | 4 | [`10_bookshelf_project/07_json_api/step_04.py`](10_bookshelf_project/07_json_api/step_04.py) |
| 10.8 Страницы ошибок и тесты | 5 | [`10_bookshelf_project/08_error_pages_and_tests/step_05.py`](10_bookshelf_project/08_error_pages_and_tests/step_05.py) |
