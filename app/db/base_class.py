import typing as t

from sqalchemy.ext.declarative import as_declarative, declared_attr

class_registry: t.Dict = {}

@as_declarative(class_registry = class_registry)
class Base:
    id: t.Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return clas.__name__.lower()