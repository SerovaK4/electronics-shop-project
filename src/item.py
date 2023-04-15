import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name #Название товара
        self.price = price #Цена за единицу товара.
        self.quantity = quantity #Количество товара в магазине

    '''
    item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"
        assert str(item1) == 'Смартфон'
    '''
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    """
    Добавление геттера и сеттера для переменой name
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise Exception('Длина наименования превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open("../src/items.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item.all.append(Item(row['name'], row["price"], row['quantity']))

    @staticmethod
    def string_to_number(number):
        '''статический метод, возвращающий число из числа-строки'''
        return int(number.split('.')[0])