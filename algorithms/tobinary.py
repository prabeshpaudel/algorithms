class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def tobinary(integer):
    s = Stack()
    bin = 0
    while integer > 0:
        s.push(integer%2)
        integer = int(integer/2)
    while not s.isEmpty():
        bin = 10*bin + s.pop()
    
    return bin

print(tobinary(34522))

print(1000011011011010 == tobinary(34522))