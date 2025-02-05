def fast_power(a, n):
    # Базовый случай: если степень равна 0
    if n == 0:
        return 1
    # Если степень четная
    elif n % 2 == 0:
        half_power = fast_power(a, n // 2)
        return half_power * half_power
    # Если степень нечетная
    else:
        return a * fast_power(a, n - 1)


input_data = input("введите два числа через пробел (a, n): ")
a, n = map(int, input_data.split())

result = fast_power(a, n)
print(result)
