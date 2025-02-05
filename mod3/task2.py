print(", ".join([bin(int(n))[2:], oct(int(n))[2:], hex(int(n))[2:]])
      if (n := input('введите натуральное число: ').strip()).isdigit()
      and int(n) > 0 else "неверный ввод")
