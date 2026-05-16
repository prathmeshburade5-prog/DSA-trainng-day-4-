import sys

class Stacks:

    def __init__(self):

        self.stack=[]
        self.top=-1


    def push(self,ele):

        self.top=self.top+1
        self.stack.append(ele)

        print(ele,"is pushed")


    def isEmpty(self):

        if self.top==self.top-1:
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


    def traverse(self):

        for i in range(self.top,-1,-1):

            print(self.stack[i])


    def peek(self):
        pass



if __name__ == '__main__':

    obj=Stacks()

    while True:

        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch=int(input("Select any choice:"))

        if ch==1:

            ele=int(input("Enter an Element:"))
            obj.push(ele)

        elif ch==2:

            obj.pop()

        elif ch==3:

            obj.peek()

        elif ch==4:

            obj.traverse()

        elif ch==0:

            sys.exit(0)