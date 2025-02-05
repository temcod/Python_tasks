number_input = input("введите натуральное число: ")

if not number_input.isdigit() or int(number_input) <= 0:
    print("Неверный ввод")
else:
    number = int(number_input)

binary = ""
temp_number = number
while temp_number > 0:
    binary = str(temp_number % 2) + binary
    temp_number //= 2
binary = binary if binary else "0"

octal = ""
temp_number = number
while temp_number > 0:
    octal = str(temp_number % 8) + octal
    temp_number //= 8
octal = octal if octal else "0"

hex_chars = "0123456789ABCDEF"
hexadecimal = ""
temp_number = number
while temp_number > 0:
    remainder = temp_number % 16
    hexadecimal = hex_chars[remainder] + hexadecimal
    temp_number //= 16
hexadecimal = hexadecimal if hexadecimal else "0"

print(f"{binary}, {octal}, {hexadecimal}")
