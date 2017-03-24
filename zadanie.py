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
t = open('E:/test.txt')
t = t.read()
t = t.split(' ')
s = Stack()

z = u"+*/-"
for i in t:
     if i not in z:
          s.push(i)
     else:
          a = int(s.pop())
          b = int(s.pop())
          if (i == '*'):
               o = a*b
               s.push(o)
          elif (i == '/'):
               o = b/a    
               s.push(o)
          elif (i == "+"):
               o = a+b
               s.push(o)
          elif (i == '-'):
               o = b-a
               s.push(o)
print(s.peek())


