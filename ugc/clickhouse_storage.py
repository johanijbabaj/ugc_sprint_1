import backoff
from clickhouse_driver import Client
from clickhouse_driver.errors import Error


class ClickHouseStorage:

    def __init__(self, ch: Client):
        self.ch = ch

    @backoff.on_exception(
        backoff.expo,
        Error,
        max_tries=3)
    def execute_query(self, query, params=None):
        return self.ch.execute(query, params)

    