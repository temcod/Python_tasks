def analyze_numbers(numbers):
    # Проверяем, все ли числа равны
    if all(num == numbers[0] for num in numbers):
        return "все числа равны"
    # Проверяем, все ли числа разные
    elif len(numbers) == len(set(numbers)):
        return "все числа разные"
    # Если ни одно из условий не выполнено
    else:
        return "есть равные и неравные числа"


input_data = input("Введите числа через пробел: ")
numbers = list(map(int, input_data.split()))

result = analyze_numbers(numbers)
print(result)
