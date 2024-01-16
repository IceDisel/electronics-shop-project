import pytest

from src.keyboard import Keyboard


@pytest.fixture
def product_kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(product_kb):
    assert str(product_kb) == "Dark Project KD87A"

    product_kb.change_lang()
    assert str(product_kb.language) == "RU"

    product_kb.change_lang()
    assert str(product_kb.language) == "EN"

    assert repr(product_kb) == "Keyboard('Dark Project KD87A', 9600, 5) EN"

    with pytest.raises(AttributeError):
        product_kb.language = 'CH'
