input_data = input('введите номер телефона: ')

# Удаление лишних символов
result = ""
for char in input_data:
    if char.isdigit() or char == '+':
        result += char

print(result)
