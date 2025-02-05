class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            raise IndexError("Очередь пуста")
        val = self.start.data
        self.start = self.start.nref
        if self.start:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        index = 0
        while current and index < n - 1:
            current = current.nref
            index += 1

        if current is None:
            raise IndexError("Индекс вне диапазона")

        new_node = Node(val)
        new_node.nref = current.nref
        new_node.pref = current
        if current.nref:
            current.nref.pref = new_node
        current.nref = new_node
        if new_node.nref is None:
            self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого очереди
        """
        current = self.start
        result = []
        while current:
            result.append(current.data)
            current = current.nref
        print(" <-> ".join(map(str, result)))


# Пример использования
if __name__ == "__main__":
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(30)
    queue.print()
    print("Pop:", queue.pop())
    queue.print()
    queue.insert(1, 25)
    queue.print()
