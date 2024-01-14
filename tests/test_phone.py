import pytest

from src.phone import Phone


@pytest.fixture
def product_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(product_phone: Phone) -> None:
    """
    Тест проверки аргументов экземпляра класса
    """
    assert product_phone.name == "iPhone 14"
    assert product_phone.price == 120000
    assert product_phone.quantity == 5
    assert product_phone.number_of_sim == 2


def test_repr(product_phone: Phone) -> None:
    """
    Тест магического метода repr
    """
    assert repr(product_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_setter(product_phone: Phone) -> None:
    """
    Тест сеттера
    """
    product_phone.number_of_sim = 3
    assert product_phone.number_of_sim == 3

    with pytest.raises(ValueError):
        product_phone.number_of_sim = 0
    with pytest.raises(ValueError):
        product_phone.number_of_sim = -2
