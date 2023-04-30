import csv
import os

from csv import DictReader


class InstantiateCSVError(Exception):
    """
    Класс для обработки собственных исключений
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
            """
            Считывает файл и создает экземпляры класса Item
            """
            f_path = "../src/items.csv"

            try:
                with open(f_path) as csvfile:
                    reader = DictReader(csvfile)

                    if len(reader.fieldnames) < 3:
                        raise InstantiateCSVError

                    for line in reader:
                        cls(line["name"], line["price"], line["quantity"])

            except FileNotFoundError as e:
                print(f'Отсутствует файл item.csv')

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"
