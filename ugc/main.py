from clickhouse_driver import Client
from clickhouse_storage import ClickHouseStorage

ch = ClickHouseStorage(Client(host='localhost'))

ch.execute_query('INSERT INTO shard.test (id, event_time) VALUES (1, 10), (2, 20)')
r = ch.execute_query('SELECT * FROM shard.test')


print(r)


