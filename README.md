# Информация для Наставника.

- Описание используемых технологий находится тут:
[here](docs/description.md)
- Описание API:
/docs/swagger_auth_api.yaml
- Схема базы данных:
/schema/db_schema.sql
- ORM модели:
/flask_app/db_models.py

# Информация для ревьювера
Ссылка на репозиторий
https://github.com/johanijbabaj/Auth_sprint_2.git

## Запуск основного docker-compose с сервисами авторизации:

[here](docker-compose.yml)
Предварительно:
* убрать у файла [here](auth.env.example) расщирение example
* убрать у файла [here](db_auth.env.example) расширение example
* Для заведения нового Oauth провайдера необходимо добавить параметры провайдера в файл auth.env параметры провайдера.
Все значения параметров должны быть в верхнем регистре и начинатся с названия провайдера, например YANDEX..., GOOGLE...
и т.д.


После запуска по адресу [url](http://flask_auth_api:5000/apidocs/) swagger схема с описанием для проверки работы сервисов

## Запуск docker-compose c тестами:

[here](tests/auth_api/docker-compose.yml)
Предварительно:
* убрать у файла [here](tests/auth_api/auth.env.example) расширение example
* убрать у файла [here](tests/auth_api/db_auth.env.example) расширение example
