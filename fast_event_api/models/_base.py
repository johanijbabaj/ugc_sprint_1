import orjson
from pydantic import BaseModel


def orjson_dumps(v):
    """
    Аналог orjson.dumps. Возвращает строку unicode а не bytes,
    так нужно для pydantic
    """
    return orjson.dumps(v).decode("utf-8")


class OrjsonModel(BaseModel):
    def toJSON(self):
        return orjson.dumps(self, default=lambda o: o.__dict__)

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
