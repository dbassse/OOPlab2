from task_package.zad1 import Pair
def main():
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



if __name__ == "__main__":
    main()
    