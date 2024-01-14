"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.fixture
def product() -> Item:
    return Item("Смартфон", 10000, 20)


def test_init(product: Item) -> None:
    """
    Тест проверки аргументов экземпляра класса
    """
    assert product.name == "Смартфон"
    assert product.price == 10000
    assert product.quantity == 20


def test_item() -> None:
    """
    Тест проверки аргументов класса
    """
    assert Item.pay_rate == 1.0
    Item.pay_rate = 0.5
    assert Item.pay_rate == 0.5
    assert len(Item.all) == 1


def test_price_discount(product: Item):
    """
    Тест проверки методов
    """
    assert product.calculate_total_price() == 10000
    product.apply_discount()
    assert product.calculate_total_price() == 5000


def test_name(product):
    """
    Тестирование сеттера name
    """
    product.name = "СуперТелефон"
    assert product.name == "СуперТелеф"
    product.name = "Телефон"
    assert product.name == "Телефон"


def test_string_to_number(product: Item) -> None:
    """
    Тестирование статик метода возвращающий число из числа-строки
    """
    assert product.string_to_number('5') == 5
    assert product.string_to_number('5.0') == 5
    assert product.string_to_number('5.5') == 5
    assert product.string_to_number('abc') is None


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 9
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 10000
    assert Item.all[0].quantity == 20
    assert Item.all[1].name == 'Смартфон'
    assert Item.all[1].price == 5000.0
    assert Item.all[1].quantity == 20
    assert Item.all[2].name == 'Телефон'
    assert Item.all[2].price == 10000
    assert Item.all[2].quantity == 20


def test_str_and_repr(product):
    assert repr(product) == "Item('Смартфон', 10000, 20)"
    assert str(product) == 'Смартфон'


def test__add__(product):
    """
    Тестирование сложения количества товаров
    """
    assert product + product == 40
