from api import User
import pytest


def test_all_values_correct_in_response():
    """Положительный тест на полное соответствие всех значений в теле ответа (response) валидным значениям шаблона
    - модели данных BaseModel библиотеки Pydantic. Для тестов по правилам ОПП определен класс User в отдельном
    файле api.py."""

    response = {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "ghostbusters", "email": "ghostbusters1984@gmail.com"}

    User(**response)


def test_incorrect_password_min_length_in_response():
    """Негативный тест на несоответствие минимального количества символов в значении ключа password в теле ответа
    (response) валидному количеству символов, определенному в классе User(BaseModel). Для теста используется валидатор
    constr () библиотеки Pydantic, который вводит ограничение на содержание минимального допустимого количества символов
    в значении ключа password. Для успешного прохождения негативного теста-кейса программа должна вызвать тип ошибки
    ValidationError и выдать подсказку о невалидном количестве символов (менее 9)."""

    response = [
        {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "xxxxxxxx", "email": "ghostbusters1984@gmail.com"}
    ]
    users = [User(**user) for user in response]

    # В случае, если валидатор constr () библиотеки Pydantic не применяется, возможно проверить количество символов в
    # ответе и вызвать исключение ValueError с помощью инструкции raise:

    if len(users[0].password) <= 9:
        raise ValueError("Количество символов в значении ключа password меньше или равно 9.")
    else:
        print(" Допустимое минимальное количество символов в значении ключа password соответствует условиям.")


def test_incorrect_password_max_length_in_response():
    """Негативный тест на несоответствие максимального количества символов в значении ключа password в теле ответа
    (response) валидному количеству символов, определенному в классе User(BaseModel). Для теста используется валидатор
    constr () библиотеки Pydantic, который вводит ограничение на содержание максимально допустимого количества символов
    в значении ключа password. Для успешного прохождения негативного теста-кейса программа должна вызвать тип ошибки
    ValidationError и выдать подсказку о невалидном количестве символов (более 15)."""

    response = [
        {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 34, "country": "USA",
         "password": "xxxxxxxxxxxxxxxxxxx", "email": 'ghostbusters1984@gmail.com'},
        {"id": 2, "first_name": "Egon", "last_name": "Spengler", "age": 40, "country": "USA",
         "password": "xxxxxxxxxxxxxxxxxxx", "email": 'ghostbusters1984@gmail.com'}
    ]
    users = [User(**user) for user in response]

    # В случае, если валидатор constr () библиотеки Pydantic не применяется, возможно проверить количество символов в
    # ответе и вызвать исключение ValueError с помощью инструкции raise:

    if len(users[0].password) >= 15:
        raise ValueError("Количество символов в значении ключа password больше или равно 15.")
    else:
        print(" Максимальное количество символов в значении ключа password соответствует условиям.")


def test_incorrect_age_value_in_response():
    """Негативный тест на несоответствие значения возраста (age) в теле ответа (response) валидному значению возраста,
    определенному в классе User(BaseModel). Для теста используется валидатор conint() библиотеки Pydantic, который
    вводит ограничение на значение ключа age - возраст пользователя должен быть более 12 лет. Для успешного прохождения
    негативного теста программа должна вызвать тип ошибки ValidationError."""

    response = {"id": 1, "first_name": "Peter", "last_name": "Venkman", "age": 11, "country": "USA",
                "password": "ghostbusters", "email": "ghostbusters1984@gmail.com"}

    User(**response)


def test_incorrect_id_value_in_response():
    """Негативный тест на несоответствие значения ключа id в теле ответа (response) валидному типу значения id,
    определенному в классе User(BaseModel). Для успешного прохождения негативного теста программа c помощью библиотеки
    Pytest должна определить ошибку класса <class 'ValueError'> и успешно завершить тест. В случае если программа
    не вызывает ошибку класса <class 'ValueError'> негативный тест считается не пройденным (некорректным)."""

    response = {"id": "invalid string value", "first_name": "Peter", "last_name": "Venkman", "age": 34,
         "country": "USA", "password": "ghostbusters", "email": "ghostbusters1984@gmail.com"}

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