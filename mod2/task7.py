input_data = input()

# Разделение строки на s и i вручную
comma_index = 0
while comma_index < len(input_data) and input_data[comma_index] != ',':
    comma_index += 1

s = input_data[:comma_index]  # Строка до запятой
i = input_data[comma_index + 1]  # Символ после запятой

# Подсчет символов i в начале строки
count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)
