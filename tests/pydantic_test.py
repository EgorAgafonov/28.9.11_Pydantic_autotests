from api import User
import pytest


def test_all_values_correct_in_response():
    """Положительный тест на полное соответствие всех значений в теле ответа (response) валидным значениям шаблона
    - модели данных BaseModel библиотеки Pydantic. Для тестов по правилам ОПП определен класс User в отдельном
    файле api.py."""

    response = [
        {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "ghostbusters", "email": 'ghostbusters1984@gmail.com'}
        ]

    users = [User(**user) for user in response]


def test_incorrect_age_value_in_response():
    """Негативный тест на несоответствие значения возраста (age) в теле ответа (response) валидному значению возраста,
    определенному в классе User(BaseModel). Для теста используется валидатор conint(gt=12) библиотеки Pydantic, который
    вводит ограничение на значение ключа age - возраст пользователя должен быть более 12 лет. Для успешного прохождения
    негативного теста программа должна вызвать тип ошибки ValidationError."""

    response = [
        {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 11,
         "country": "USA", "password": "ghostbusters", "email": 'ghostbusters1984@gmail.com'}
    ]
    users = [User(**user) for user in response]


def test_incorrect_id_value_in_response():
    """Негативный тест на несоответствие значения ключа id в теле ответа (response) валидному типу значения id,
    определенному в классе User(BaseModel). Для успешного прохождения негативного теста программа c помощью библиотеки
    Pytest должна вызвать ошибку класса <class 'ValueError'>. В случае если программа не вызывает ошибку класса
    <class 'ValueError'> негативный тест считается не пройденным (некорректным)."""

    response = {"id": "invalid string value", "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "ghostbusters", "email": 'ghostbusters1984@gmail.com'}

    with pytest.raises(ValueError):
        User(**response)

def test_incorrect_first_name_value_in_response():
    """Негативный тест на несоответствие значения ключа first_name в теле ответа (response) валидному типу значения
    first_name, определенному в классе User(BaseModel). Тест c помощью оператора assert сравнивает значения ключей
    first_name в теле ответа (response) и в классе User(BaseModel), затем выводит результат сравнения.
    Негативный тест считается пройденным, если сравниваемые типы данных не соответствует друг другу."""

    response = [
        {"id": 1, "first_name": 123, "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "ghostbusters", "email": 'ghostbusters1984@gmail.com'}
    ]
    users = [User(**user) for user in response]

    assert users[0].first_name == "Peter"


def test_incorrect_password_length_in_response():
    """Негативный тест на несоответствие количества символов в значении ключа password в теле ответа (response)
    валидному количеству символов, определенному в классе User(BaseModel). Для теста используется валидатор
    constr () библиотеки Pydantic, который вводит ограничение на содержание количества символов (минимальное=9
    и максимальное=15) в значении ключа password. Для успешного прохождения негативного теста-кейса программа должна
     вызвать тип ошибки ValidationError и выдать подсказку о невалидном (min и/или max) количестве символов."""

    response = [
        {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "xxx", "email": 'ghostbusters1984@gmail.com'}
    ]
    users = [User(**user) for user in response]

