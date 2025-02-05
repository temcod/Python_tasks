input_data = input('введите через пробел три слова: ')

# Инициализация переменных
words = []
current_word = ""
for char in input_data:
    if char == ' ':
        words.append(current_word)
        current_word = ""
    else:
        current_word += char
words.append(current_word)  # Добавляем последнее слово

# Составление нового слова из последних букв каждого слова
result = ""
for word in words:
    if word:  # Проверяем, что слово не пустое
        result += word[-1]

print(result)
