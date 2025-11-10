from datetime import datetime
from typing import Any, Optional


class Goods:
    MAX_SIZE = 1000

    def __init__(self, *args: Any) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            # инициализация массива "код,наименование,цена,количество"
            code_str, name, price_str, quantity_str = args[0].split(",")
            self._code = int(code_str)
            self._name = name
            self._price = float(price_str)
            self._quantity = int(quantity_str)
        else:
            # Конструктор по умолчанию
            self._code = 0
            self._name = ""
            self._price = 0.0
            self._quantity = 0

    # Получение полей данных с помощью функций get
    def get_code(self) -> int:
        return self._code

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_quantity(self) -> int:
        return self._quantity

    # Установка полей данных с помощью функций set
    def set_code(self, code: int) -> None:
        self._code = code

    def set_name(self, name: str) -> None:
        self._name = name

    def set_price(self, price: float) -> None:
        self._price = price

    def set_quantity(self, quantity: int) -> None:
        self._quantity = quantity

    def get_total(self) -> float:
        """Cтоимость за один вид товара"""
        return self._price * self._quantity

    def __str__(self) -> str:
        return f"Товар [Код: {self._code}, Наименование: {self._name}, Цена: {self._price}, Количество: {self._quantity}, Сумма: {self.get_total()}]"


class Receipt:
    MAX_SIZE = 100

    def __init__(self, receipt_number: int, size: int = MAX_SIZE) -> None:
        self._receipt_number = receipt_number
        self._date_time = datetime.now()
        self._size = size
        self._count = 0  # Текущее количество элементов
        self._goods_list: list[Optional[Goods]] = [None] * size

    def size(self) -> int:
        return self._size

    def get_count(self) -> int:
        """Возвращает текущее количество элементов"""
        return self._count

    def get_receipt_number(self) -> int:
        return self._receipt_number

    def get_date_time(self) -> datetime:
        return self._date_time

    def add_goods(self, goods: Goods) -> bool:
        """Добавление записи о покупаемом товаре"""
        if self._count >= self._size:
            return False  # Достигнут максимальный размер

        # Проверка на None для mypy
        if self._goods_list[self._count] is None:
            self._goods_list[self._count] = goods
            self._count += 1
            return True
        return False

    def update_goods(self, goods: Goods) -> bool:
        """Изменение записи о покупаемом товаре"""
        for i in range(self._count):
            current_goods = self._goods_list[i]
            # Проверка на None для mypy
            if (
                current_goods is not None
                and current_goods.get_code() == goods.get_code()
            ):
                self._goods_list[i] = goods
                return True
        return False

    def remove_goods(self, code: int) -> bool:
        """Удаление записи о покупаемом товаре по коду"""
        for i in range(self._count):
            current_goods = self._goods_list[i]
            # Проверка на None для mypy
            if current_goods is not None and current_goods.get_code() == code:
                # Сдвигаем элементы
                for j in range(i, self._count - 1):
                    self._goods_list[j] = self._goods_list[j + 1]
                self._goods_list[self._count - 1] = None
                self._count -= 1
                return True
        return False

    def find_goods_by_code(self, code: int) -> Optional[Goods]:
        for i in range(self._count):
            current_goods = self._goods_list[i]
            # Проверка на None для mypy
            if current_goods is not None and current_goods.get_code() == code:
                return current_goods
        return None

    def get_total_sum(self) -> float:
        total = 0.0
        for i in range(self._count):
            current_goods = self._goods_list[i]
            # Проверка на None для mypy
            if current_goods is not None:
                total += current_goods.get_total()
        return total

    def __getitem__(self, index: int) -> Goods:
        if index < 0 or index >= self._count:
            raise IndexError(f"Index {index} out of range [0, {self._count-1}]")

        goods = self._goods_list[index]
        # Проверка на None для mypy
        if goods is None:
            raise ValueError(f"Goods at index {index} is None")
        return goods

    def __setitem__(self, index: int, value: Goods) -> None:
        if index < 0 or index >= self._count:
            raise IndexError(f"Index {index} out of range [0, {self._count-1}]")
        self._goods_list[index] = value

    def __len__(self) -> int:
        return self._count

    def __str__(self) -> str:
        result = [f"Товарный чек №{self._receipt_number}"]
        result.append(f"Дата: {self._date_time.strftime('%Y-%m-%d %H:%M:%S')}")
        result.append(f"Товаров: {self._count}/{self._size}")
        result.append("Список товаров:")

        for i in range(self._count):
            goods = self._goods_list[i]
            # Проверка на None для mypy
            if goods is not None:
                result.append(f"  {i+1}. {goods}")

        result.append(f"Общая сумма: {self.get_total_sum():.2f}")
        return "\n".join(result)


if __name__ == "__main__":
    receipt = Receipt(12345, size=5)

    goods1 = Goods("100,Яблоки,2.5,10")
    goods2 = Goods("200,Бананы,1.8,15")
    goods3 = Goods("300,Апельсины,3.2,8")

    receipt.add_goods(goods1)
    receipt.add_goods(goods2)
    receipt.add_goods(goods3)

    print("Исходный чек:")
    print(receipt)
    print("\n" + "=" * 50)

    print("\nДоступ через индексирование:")
    for i in range(len(receipt)):
        print(f"receipt[{i}] = {receipt[i]}")

    print("\nИзменение через индексирование:")
    receipt[1] = Goods("250,Груши,2.8,12")
    print(f"После изменения: {receipt[1]}")

    print("\nПоиск товара с кодом 100:")
    found = receipt.find_goods_by_code(100)
    print(found if found else "Не найден")

    print(f"\nОбщая сумма чека: {receipt.get_total_sum():.2f}")
