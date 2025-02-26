"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


@pytest.fixture
def smartphone():
    return Item("Телевизор", 50000, 5)


def test_calculate_total_price(smartphone):
    item1 = Item("tea", 3000, 10)
    assert item1.price == 3000


def test_apply_discount():
    item1 = Item("tea", 3000, 10)
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 2400


def test___repr__(smartphone):
    assert repr(smartphone) == "Item('Телевизор', 50000, 5)"


def test___str__(smartphone):
    assert str(smartphone) == 'Телевизор'


def test_item(smartphone):
    assert smartphone.name == "Телевизор"
    assert smartphone.price == 50000
    assert smartphone.quantity == 5


@pytest.fixture()
def some_exception():
    return InstantiateCSVError()


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_exception(some_exception):
    assert str(some_exception) == 'Файл item.csv поврежден'

