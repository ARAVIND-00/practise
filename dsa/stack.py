
stack=[]
def push():
    a=int(input("enter add"))
    stack.append(a)
    print("added")
    return stack

def pop():
    if not stack :
        print("empty stack")
    
    else:
        stack.pop()
        print("removed")
        return stack
    


while True:
    print("1-p,2-p,3-q")
    
    c=int(input())
    
    if c==1:
        print(push())
    if c==2:
       print(pop()) 
       
    if c==3:
        break
    else:
        print("enter correct")