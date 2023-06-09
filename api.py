from pydantic import BaseModel


class ApiKeyRequest(BaseModel):
    access_key: str


class User(BaseModel):
    username: str
    age: int
    email: str
    password: str


class Order(BaseModel):
    id_tag: int
    name_of_product: str
    amount: str
    total_value: float

