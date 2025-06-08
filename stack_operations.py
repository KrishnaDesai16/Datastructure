class Stack:
    def __init__(self,max_size):
        self.items =[]
        self.max_size=max_size
    
    def push(self,item):
        if self.isfull():
            print("stack is overflow")
            return None
        else:
            self.items.append(item)
            print(f'pushed item {item}')
            
    def pop(self):
        if self.isempty():
            print("stack is undeflow")
            return None
        else:
            print(f'poped item '%self.items.pop())
     
    def peek(self):
        if s.isempty():
            print("stack is undeflow")
            return None
        else:
            print(f'peek item {self.items[-1]}')

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
        print(self.items)

s= Stack(2)
s.pop()
s.push(1)
s.push(2)
s.peek()
s.print_stack()



