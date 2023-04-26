import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def TV():
    return KeyBoard("Телевизор", 50000, 5)


def test_init(TV):
    assert str(TV) == "Телевизор"


def test_lang(TV):
    assert TV.language == "EN"


def test_change_lang(TV):
    TV.change_lang()
    assert TV.language == "RU"
    TV.change_lang()
    assert TV.language == "EN"
