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


def tobase(integer, base):
    digits = "0123456789ABCDE"
    s = Stack()
    num = ""
    while integer > 0:
        s.push(digits[integer%base])
        integer = int(integer/base)
    while not s.isEmpty():
        num = num + s.pop()
    
    return num

print(tobase(34522, 16))

print(1000011011011010 == int(tobase(34522, 2)))