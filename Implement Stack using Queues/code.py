class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def push(self, x: int) -> None:
        n = Node(x)
        if self.first_node is None:
            self.first_node = n
            self.last_node = n
        else:
            self.last_node.next = n
            self.last_node = n

    def pop(self) -> int:
        data = self.first_node.data
        if self.first_node == self.last_node:
            self.last_node = None
        self.first_node = self.first_node.next
        return data

    def top(self) -> int:
        return self.first_node.data

    def empty(self) -> bool:
        return self.first_node is None


class MyStack:
    def __init__(self):
        self.main_q = Queue()
        self.temp_q = Queue()

    def push(self, x: int) -> None:
        self.temp_q.push(x)
        while not self.main_q.empty():
            self.temp_q.push(self.main_q.pop())
        self.main_q, self.temp_q = self.temp_q, self.main_q

    def pop(self) -> int:
        return self.main_q.pop()

    def top(self) -> int:
        return self.main_q.top()

    def empty(self) -> bool:
        return self.main_q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()