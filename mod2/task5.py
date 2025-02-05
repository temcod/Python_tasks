domain_input = input("введите доменное имя: ")
parts = []
current_part = ""
for char in domain_input:
    if char == '.':
        parts.append(current_part)
        current_part = ""
    else:
        current_part += char
parts.append(current_part)


for part in reversed(parts):
    print(part)
