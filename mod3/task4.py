print("yes" if (s := input('введите строку из 0 и 1: ')).count(
    "1") == s.count("0") else "no")
