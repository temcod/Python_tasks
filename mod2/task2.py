side = int(input('введите длину стороны квадрата: '))
perimetr = 4 * side
area = side ** 2
diagonal = (side ** 2 + side ** 2) ** 0.5
print(f"{perimetr: .2f}, {area: .2f}, {diagonal: .2f}")
