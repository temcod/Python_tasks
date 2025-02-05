def gcd_recursive(a, b):
    # Базовый случай: если второе число равно 0
    if b == 0:
        return a
    # Рекурсивный вызов
    return gcd_recursive(b, a % b)


input_data = input("введите два числа через пробел (a, b): ")
a, b = map(int, input_data.split())

# Вывод результата
result = gcd_recursive(a, b)
print(result)
