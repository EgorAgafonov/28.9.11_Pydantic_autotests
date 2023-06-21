from pydantic import BaseModel
from pydantic import conint
from pydantic import EmailStr
from pydantic import constr


class User(BaseModel):
    """Класс User для тестирования ответов REST API-сервисов на основе класса BaseModel библиотеки Pydantic.
    Для целей тестирования данных, передаваемых в ответах API-сервисов, каждое поле класса User имеет свой валидатор,
    предусмотренный библиотекой Pydantic."""

    id: conint(strict=int)
    first_name: constr(strict=str)
    last_name: constr(strict=str)
    age: conint(gt=12)
    country: constr(strict=str)
    password: constr(min_length=9, max_length=15)
    email: EmailStr


