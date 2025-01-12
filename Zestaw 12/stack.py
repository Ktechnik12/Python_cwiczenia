class UniqueStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.exists = [0] * size

    def push(self, value):
        if value < 0 or value >= self.size:
            raise ValueError(f"Value {value} is out of bounds (0 to {self.size - 1}).")
        
        if self.exists[value] == 0:
            self.stack.append(value)
            self.exists[value] = 1

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from an empty stack.")
        
        value = self.stack.pop()
        self.exists[value] = 0
        return value

    def peek(self):
        if not self.stack:
            raise IndexError("Peek from an empty stack.")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return f"Stack: {self.stack}, Exists: {self.exists}"


size = 10
stack = UniqueStack(size)

stack.push(3)
stack.push(5)
stack.push(3)
stack.push(1)

print(stack)

stack.pop()
print(stack)
