import csv
import os


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        try:
            if not isinstance(other, self.__class__):
                raise TypeError("Невозможно выполнить сложение с разными типами")
            return self.quantity + other.quantity
        except TypeError as e:
            return str(e)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price

    @classmethod
    def instantiate_from_csv(cls, filename=''):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Отсутствует файл {os.path.basename(filename)}")
            with open(filename, mode='r') as file:
                data = csv.DictReader(file)

                for row in data:
                    if not ('name' in row and 'price' in row and 'quantity' in row) or None in row.values():
                        raise InstantiateCSVError(f"Файл {os.path.basename(filename)} поврежден")

                    cls(row['name'], float(row['price']), int(row['quantity']))

        except (FileNotFoundError, KeyError, ValueError, InstantiateCSVError) as e:
            print(type(e).__name__ + ": " + str(e))

    @staticmethod
    def string_to_number(string: str) -> int | None:
        """
        Статик метод возвращающий число из числа-строки
        """
        try:
            number = int(float(string))
            return number
        except ValueError:
            return None

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


class InstantiateCSVError(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message
