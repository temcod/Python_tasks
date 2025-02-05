a = input('введите первое число: ')
b = input('введите второе число: ')
c = input('введите третье число: ')
a = int(a)
b = int(b)
c = int(c)

if (a >= b >= c) or (c >= b >= a):
    print(b)
elif (b >= a >= c) or (c >= a >= b):
    print(a)
else:
    print(c)
