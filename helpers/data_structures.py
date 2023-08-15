import json
from typing import NamedTuple, Type, TypeVar

T = TypeVar("T", bound=NamedTuple)


def load_namedtuple_from_json(json_file: str, data_structure_class: Type[T]) -> T:
    with open(json_file, "r") as file:
        data = json.load(file)

    return data_structure_class(**data)


class UserRegistration(NamedTuple):
    email: str
    password: str

    @classmethod
    def from_json(cls, json_file: str) -> "UserRegistration":
        return load_namedtuple_from_json(json_file, cls)