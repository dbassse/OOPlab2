import math
from typing import Any, Iterator, Union


class Pair:
    """Класс для работы с координатами точки
    с использованием перегрузки операторов"""

    def __init__(self, first: float = 0.0, second: float = 0.0) -> None:
        try:
            self.first = float(first)
            self.second = float(second)
        except (ValueError, TypeError) as e:
            raise ValueError("Введите дробное число Float") from e

    def __str__(self) -> str:
        return f"({self.first}, {self.second})"

    def __repr__(self) -> str:
        return f"Pair({self.first}, {self.second})"

    def __abs__(self) -> float:
        return math.sqrt(self.first**2 + self.second**2)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Pair):
            return False
        return math.isclose(self.first, other.first) and math.isclose(
            self.second, other.second
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __add__(self, other: "Pair") -> "Pair":
        if not isinstance(other, Pair):
            raise TypeError("Можно складывать только объекты Pair")
        return Pair(self.first + other.first, self.second + other.second)

    def __sub__(self, other: "Pair") -> "Pair":
        if not isinstance(other, Pair):
            raise TypeError("Можно вычитать только объекты Pair")
        return Pair(self.first - other.first, self.second - other.second)

    def __mul__(self, scalar: Union[float, int]) -> "Pair":
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Можно умножать только на число")
        return Pair(self.first * scalar_float, self.second * scalar_float)

    def __rmul__(self, scalar: Union[float, int]) -> "Pair":
        """Умножение скаляра на координаты (правая сторона)"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[float, int]) -> "Pair":
        """Деление координат на скаляр"""
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Можно делить только на число")
        if scalar_float == 0:
            raise ZeroDivisionError("Деление на ноль")
        return Pair(self.first / scalar_float, self.second / scalar_float)

    def __iadd__(self, other: "Pair") -> "Pair":
        """+= оператор"""
        if not isinstance(other, Pair):
            raise TypeError("Можно складывать только объекты Pair")
        self.first += other.first
        self.second += other.second
        return self

    def __isub__(self, other: "Pair") -> "Pair":
        """-= оператор"""
        if not isinstance(other, Pair):
            raise TypeError("Можно вычитать только объекты Pair")
        self.first -= other.first
        self.second -= other.second
        return self

    def __imul__(self, scalar: Union[float, int]) -> "Pair":
        """*= оператор"""
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Можно умножать только на число")
        self.first *= scalar_float
        self.second *= scalar_float
        return self

    def __itruediv__(self, scalar: Union[float, int]) -> "Pair":
        """/= оператор"""
        try:
            scalar_float = float(scalar)
        except (ValueError, TypeError):
            raise TypeError("Можно делить только на число")
        if scalar_float == 0:
            raise ZeroDivisionError("Деление на ноль")
        self.first /= scalar_float
        self.second /= scalar_float
        return self

    def __bool__(self) -> bool:
        """Проверка, не является ли точка началом координат"""
        return not (math.isclose(self.first, 0.0) and math.isclose(self.second, 0.0))

    def __len__(self) -> int:
        return 2

    def __iter__(self) -> Iterator[float]:
        yield self.first
        yield self.second

    def read(self) -> None:
        """Чтение координат с клавиатуры"""
        try:
            self.first = float(input("Введите первую координату x: "))
            self.second = float(input("Введите вторую координату y: "))
        except ValueError as e:
            raise ValueError("Введите число!") from e

    def display(self) -> None:
        """Вывод координат на экран"""
        print(f"Координаты точки х и y: ({self.first}, {self.second})")

    def distance(self) -> float:
        """Расстояние от начала координат до точки"""
        return abs(self)

    def make_pair(self, first: Union[float, int], second: Union[float, int]) -> None:
        """Установка новых значений координат"""
        try:
            self.first = float(first)
            self.second = float(second)
        except (ValueError, TypeError) as e:
            raise ValueError("Введите дробное число Float") from e


if __name__ == "__main__":
    point1 = Pair(1.2, 2.4)
    point2 = Pair(3.1, 1.5)

    print("Точка 1:", point1)
    print("Точка 2:", point2)
    print("Расстояние до точки 1:", point1.distance())
    print("Модуль точки 1:", abs(point1))

    print("\nАрифметические операции:")
    print("point1 + point2 =", point1 + point2)
    print("point1 - point2 =", point1 - point2)
    print("point1 * 2 =", point1 * 2)
    print("3 * point1 =", 3 * point1)
    print("point1 / 2 =", point1 / 2)

    point3 = Pair(1, 1)
    point3 += point1
    print("point3 += point1 ->", point3)

    point3 *= 2
    print("point3 *= 2 ->", point3)

    print("\nСравнение:")
    print("point1 == point2:", point1 == point2)
    print("point1 != point2:", point1 != point2)

    print("\nБулева проверка:")
    zero_point = Pair(0, 0)
    print("point1 не нулевая:", bool(point1))
    print("zero_point нулевая:", bool(zero_point))

    print("\nИтерация:")
    for coord in point1:
        print("Координата:", coord)
