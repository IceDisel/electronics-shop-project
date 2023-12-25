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
