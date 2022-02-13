# Информация для Наставника.

- Описание используемых технологий находится тут:
[here](/docs/description.md)
- Описание API:
/docs/swagger_auth_api.yaml
- Схема базы данных:
/schema/db_schema.sql
- ORM модели:
/flask_app/db_models.py
- Описание схемы сервисов AS_IS на начала 8 спринта
- Описание схемы сервисов TO_BE на конец 8 спринта
[here](/docs/asis_service_architecture.puml)

# Информация для ревьювера
Ссылка на репозиторий
https://github.com/johanijbabaj/ugc_sprint_1.git


## Запуск docker-compose с сервисом UGC:
[Ссылка на отдельный docker-compose файл для сервиса обработки генерируемого клиентом контента](docker-compose_ugc.yml)

Предварительно:
* убрать у файла [here](fa.env.example) расширение example

ETL по перекачки данных из Kafka в Clickhouse выполнен с  помощью таблиц в clickhouse с [движком kafka](https://clickhouse.com/docs/ru/engines/table-engines/integrations/kafka/).
Для создания необходимых таблиц в Clickhouse необходимо выполнить команды:
* Выполнить команду <code>docker exec -ti clickhouse-node1 bash /tmp/init-db-shard1.sh</code>
* Выполнить команду <code>docker exec -ti clickhouse-node3 bash /tmp/init-db-shard2.sh</code>

После запуска по адресу [url](http://fast_event_api:8000/api/openapi#/) swagger схема с описанием для проверки работы сервисов
