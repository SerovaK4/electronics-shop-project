# Режимы доступа. Домашнее задание

## Описание задачи

Внесите следующие изменения в класс `Item`:

- атрибут `name` сделать приватным
- добавить геттер и сеттер для `name`, используя @property
- в сеттере `name` проверять, что длина наименования товара не больше 10 симвовов

Добавьте в `Item` следующие методы:
- `instantiate_from_csv()` - класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
- `string_to_number()` - статический метод, возвращающий число из числа-строки

Тестирование:
- Напишите тесты для новых методов в `tests/test_item.py`

## Ожидаемое поведение
- Код в файле `main.py` должен выдавать ожидаемые значения