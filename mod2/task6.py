s = input('введите строку, которая состоит из 0 и 1: ')
zeros = 0
ones = 0
for char in s:
    if char == '0':
        zeros += 1
    elif char == '1':
        ones += 1

if zeros == ones:
    print('yes')
else:
    print('no')
