def can_form_palindrome(s):
    # Подсчитываем частоту каждого символа
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Считаем количество символов с нечетной частотой
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1

    # Если больше одного символа с нечетной частотой, палиндром невозможен
    if odd_count > 1:
        return "палиндром составить нельзя"

    # Формируем первую половину палиндрома
    first_half = ""
    middle_char = ""
    for char, count in char_counts.items():
        if count % 2 == 0:
            first_half += char * (count // 2)
        else:
            middle_char = char
            first_half += char * (count // 2)

    # Собираем палиндром
    palindrome = first_half + middle_char + first_half[::-1]
    return palindrome


input_data = input("введите строку: ")


result = can_form_palindrome(input_data)
print(result)
