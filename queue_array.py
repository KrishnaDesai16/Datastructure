from collections import deque

class Queue:
    def __init__(self,max_size):
        self.items = deque()
        self.max_size=max_size
    
    def enqueue(self,item):
        if self.isfull():
            print("queue is overflow")
            return None
        else:
            self.items.append(item)
            print(f'added item at rear {item}')
            
    def dqueue(self):
        if self.isempty():
            print("queue is empty")
            return None
        else:
            print(f'removed item from the {self.items.popleft()}')
     
    def peek(self):
        if self.isempty():
            print("queue is undeflow")
            return None
        else:
            print(f'peek item {self.items[0]}')

    def isfull(self):
        if len(self.items)==self.max_size:
            return True
        else:
            return False
        
    def isempty(self):
        if len(self.items)==0:
            return True
        else:
            return False
        
    def print_stack(self):
        print("Queue (front → rear):", self.items)


s= Queue(3)
s.enqueue(1)
s.enqueue(3)
s.enqueue(5)
s.dqueue()
s.enqueue(45)
s.peek()
s.print_stack()
