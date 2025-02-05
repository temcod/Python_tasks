class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise IndexError("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        current = self.end
        result = []
        while current:
            result.append(current.data)
            current = current.pref
        print(" -> ".join(map(str, reversed(result))))


# Пример использования
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print()
    print("Pop:", stack.pop())
    stack.print()
