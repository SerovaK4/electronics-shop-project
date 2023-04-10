"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Смартфон", 50000, 5)


def test_calculate_total_price(smartphone):
    item1 = Item("tea", 3000, 10)
    assert item1.price == 3000


def test_apply_discount(smartphone):
    Item.pay_rate = 0.8
    smartphone.apply_discount()
    assert smartphone.price == 40000.0


def test_name(smartphone):
    assert smartphone.name == "Смартфон"


def test_instantiate_from_csv(cls):

    print()






def test_string_to_number(smartphone):
    assert smartphone.string_to_number("3") == 3






