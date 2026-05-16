import sys
class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
        
    def isFull(self):
        if self.top==self.CAPACITY-1:
            return True
        else :
            return False
        
    
        
        
    def push(self,ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele,"is pushed")
            
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
        
    def pop(self):

        if self.isEmpty():
            

            print("Stack is Empty")

        else:
  
            ele=self.stack[self.top]

            self.stack.pop()

            self.top=self.top-1

            print(ele,"is popped")
            return ele
    
    
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
            
            
    def peek(self):
        pass
    


if __name__ == '__main__':
    obj=Stacks()
    arr=[10,20,30,40,50]
    

    for i in range(len(arr)):
        obj.push(arr[i])
    rev=[]
    for i in range(len(arr)):
            rev.append(obj.pop())
            
print("Reversed:",rev)
    