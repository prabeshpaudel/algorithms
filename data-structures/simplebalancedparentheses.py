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

def checker(pc):
    s = Stack()
    balanced = True
    for i in range(len(pc)):
        if pc[i] == "(":
            s.push("(")
        else:
            if s.size() != 0:
                s.pop()
            else:
                balanced = False
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(checker('((()))'))
print(checker('(()'))