from pydantic import BaseModel
from pydantic import conint
from pydantic import EmailStr
from pydantic import constr


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: conint(gt=12)
    country: str
    password: str
    email: EmailStr


