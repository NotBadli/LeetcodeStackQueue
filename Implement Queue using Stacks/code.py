class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.first_node = None

    def push(self, x: int) -> None:
        n = Node(x)
        nxt = self.first_node
        n.next = nxt
        self.first_node = n

    def pop(self) -> int:
        if not self.first_node:
            return None
        output = self.first_node.data
        self.first_node = self.first_node.next
        return output

    def peek(self) -> int:
        if not self.first_node:
            return None
        return self.first_node.data

    def empty(self) -> bool:
        return not self.first_node

class MyQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()