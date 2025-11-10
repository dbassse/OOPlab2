import math
import os
import sys
from io import StringIO
from unittest.mock import patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task_package.zad1 import Pair  # noqa: E402


class TestPair:
    def test_initialization_default(self):
        pair = Pair()
        assert math.isclose(pair.first, 0.0)
        assert math.isclose(pair.second, 0.0)

    def test_initialization_with_values(self):
        pair = Pair(1.5, 2.5)
        assert math.isclose(pair.first, 1.5)
        assert math.isclose(pair.second, 2.5)

    def test_initialization_with_ints(self):
        pair = Pair(1, 2)
        assert math.isclose(pair.first, 1.0)
        assert math.isclose(pair.second, 2.0)

    def test_initialization_invalid_type(self):
        with pytest.raises(ValueError, match="Введите дробное число Float"):
            Pair("invalid", "values")

    def test_str_representation(self):
        pair = Pair(1.5, 2.5)
        assert str(pair) == "(1.5, 2.5)"

    def test_repr_representation(self):
        pair = Pair(1.5, 2.5)
        assert repr(pair) == "Pair(1.5, 2.5)"

    def test_abs_method(self):
        pair = Pair(3.0, 4.0)
        assert math.isclose(abs(pair), 5.0)

        pair_zero = Pair(0.0, 0.0)
        assert math.isclose(abs(pair_zero), 0.0)

    def test_equality(self):
        pair1 = Pair(1.5, 2.5)
        pair2 = Pair(1.5, 2.5)
        pair3 = Pair(1.6, 2.5)

        assert pair1 == pair2
        assert pair1 != pair3
        assert not (pair1 == pair3)

    def test_equality_with_different_type(self):
        pair = Pair(1.5, 2.5)
        assert pair != "not a pair"

    def test_addition(self):
        pair1 = Pair(1.0, 2.0)
        pair2 = Pair(3.0, 4.0)
        result = pair1 + pair2

        assert math.isclose(result.first, 4.0)
        assert math.isclose(result.second, 6.0)

    def test_addition_invalid_type(self):
        pair = Pair(1.0, 2.0)
        with pytest.raises(TypeError, match="Можно складывать только объекты Pair"):
            pair + "invalid"

    def test_subtraction(self):
        pair1 = Pair(5.0, 6.0)
        pair2 = Pair(1.0, 2.0)
        result = pair1 - pair2

        assert math.isclose(result.first, 4.0)
        assert math.isclose(result.second, 4.0)

    def test_subtraction_invalid_type(self):
        pair = Pair(1.0, 2.0)
        with pytest.raises(TypeError, match="Можно вычитать только объекты Pair"):
            pair - "invalid"

    def test_multiplication(self):
        pair = Pair(2.0, 3.0)
        result = pair * 3.0

        assert math.isclose(result.first, 6.0)
        assert math.isclose(result.second, 9.0)

    def test_right_multiplication(self):
        pair = Pair(2.0, 3.0)
        result = 3.0 * pair

        assert math.isclose(result.first, 6.0)
        assert math.isclose(result.second, 9.0)

    def test_multiplication_invalid_type(self):
        pair = Pair(1.0, 2.0)
        with pytest.raises(TypeError, match="Можно умножать только на число"):
            pair * "invalid"

    def test_division(self):
        pair = Pair(6.0, 9.0)
        result = pair / 3.0

        assert math.isclose(result.first, 2.0)
        assert math.isclose(result.second, 3.0)

    def test_division_by_zero(self):
        pair = Pair(6.0, 9.0)
        with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
            pair / 0.0

    def test_division_invalid_type(self):
        pair = Pair(1.0, 2.0)
        with pytest.raises(TypeError, match="Можно делить только на число"):
            pair / "invalid"

    def test_inplace_addition(self):
        pair1 = Pair(1.0, 2.0)
        pair2 = Pair(3.0, 4.0)
        pair1 += pair2

        assert math.isclose(pair1.first, 4.0)
        assert math.isclose(pair1.second, 6.0)

    def test_inplace_subtraction(self):
        pair1 = Pair(5.0, 6.0)
        pair2 = Pair(1.0, 2.0)
        pair1 -= pair2

        assert math.isclose(pair1.first, 4.0)
        assert math.isclose(pair1.second, 4.0)

    def test_inplace_multiplication(self):
        pair = Pair(2.0, 3.0)
        pair *= 3.0

        assert math.isclose(pair.first, 6.0)
        assert math.isclose(pair.second, 9.0)

    def test_inplace_division(self):
        pair = Pair(6.0, 9.0)
        pair /= 3.0

        assert math.isclose(pair.first, 2.0)
        assert math.isclose(pair.second, 3.0)

    def test_boolean_conversion(self):
        pair_non_zero = Pair(1.0, 2.0)
        pair_zero = Pair(0.0, 0.0)

        assert bool(pair_non_zero) is True
        assert bool(pair_zero) is False

    def test_length(self):
        pair = Pair(1.0, 2.0)
        assert len(pair) == 2

    def test_iteration(self):
        pair = Pair(1.5, 2.5)
        coordinates = list(pair)

        assert len(coordinates) == 2
        assert math.isclose(coordinates[0], 1.5)
        assert math.isclose(coordinates[1], 2.5)

    def test_distance_method(self):
        pair = Pair(3.0, 4.0)
        assert math.isclose(pair.distance(), 5.0)

    def test_make_pair_method(self):
        pair = Pair()
        pair.make_pair(5.0, 10.0)

        assert math.isclose(pair.first, 5.0)
        assert math.isclose(pair.second, 10.0)

    def test_make_pair_invalid_type(self):
        pair = Pair()
        with pytest.raises(ValueError, match="Введите дробное число Float"):
            pair.make_pair("invalid", "values")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_method(self, mock_stdout):
        pair = Pair(1.5, 2.5)
        pair.display()

        output = mock_stdout.getvalue()
        assert "Координаты точки х и y: (1.5, 2.5)" in output

    @patch("builtins.input", side_effect=["3.5", "4.5"])
    def test_read_method(self, mock_input):
        pair = Pair()
        pair.read()

        assert math.isclose(pair.first, 3.5)
        assert math.isclose(pair.second, 4.5)

    @patch("builtins.input", side_effect=["invalid", "input"])
    def test_read_method_invalid_input(self, mock_input):
        pair = Pair()
        with pytest.raises(ValueError, match="Введите число!"):
            pair.read()

    def test_comprehensive_operations(self):
        # Создание точек
        p1 = Pair(2.0, 3.0)
        p2 = Pair(1.0, 1.0)

        # Арифметические операции
        result_add = p1 + p2
        result_sub = p1 - p2
        result_mul = p1 * 2.0
        result_div = p1 / 2.0

        assert result_add == Pair(3.0, 4.0)
        assert result_sub == Pair(1.0, 2.0)
        assert result_mul == Pair(4.0, 6.0)
        assert result_div == Pair(1.0, 1.5)

        # In-place операции
        p3 = Pair(5.0, 5.0)
        p3 += p1
        assert p3 == Pair(7.0, 8.0)

        p3 *= 2.0
        assert p3 == Pair(14.0, 16.0)

        # Проверка модуля
        assert math.isclose(abs(Pair(3.0, 4.0)), 5.0)


# Дополнительные тесты для проверки граничных случаев
class TestPairEdgeCases:
    def test_very_small_numbers(self):
        pair = Pair(1e-10, 2e-10)
        assert math.isclose(pair.first, 1e-10)
        assert math.isclose(pair.second, 2e-10)

    def test_very_large_numbers(self):
        pair = Pair(1e10, 2e10)
        assert math.isclose(pair.first, 1e10)
        assert math.isclose(pair.second, 2e10)

    def test_negative_numbers(self):
        pair = Pair(-3.0, -4.0)
        assert math.isclose(abs(pair), 5.0)

    def test_nan_handling(self):
        # Этот тест показывает, что класс не обрабатывает NaN специально
        pair = Pair(float("nan"), 1.0)
        assert math.isnan(pair.first)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
