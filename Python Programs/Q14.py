def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk, item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item

def Peek(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]


def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top] , 'is the top')
        for a in range(top-1, -1, -1):
            print(stk[a])

Stack=[]
top=None
while True:
            print("STACK OPERATIONS")
            print("0. Exit")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Display Stack")
            c=int(input("Enter your choice: "))
            if c==1:
                item=int(input("Enter item: "))
                Push(Stack, item)
            elif c==2:
                item=Pop(Stack)
                if item=="underflow":
                    print("Underflow! Stack is empty")
                else:
                    print("Popped item is: ", item)
              
                
            elif c==3:
                item=Peek(Stack)
                if item=="underflow":
                    print("Underflow! Stack is empty")

                else:
                    print("Topmost item is ", item)
            elif c==4:
                Display(Stack)

            elif c==0:
                break
            else:
                print("Invalid choice!")
                

        
