a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no. : "))
s=input("ENter the operator : ")
def add():
    c=a+b
    print(c)
def diff():
    if(a>b):
        c=a-b 
    else:
        c=b-a
    print(c)
def multiply():
    c=a*b
    print(c)
def modulo():
    if(a>b):
        c=a%b 
    else:
        c=b%a
    print(c)    
def div():
    if(a>b):
        c=a/b 
    else:
        c=b/a
    print(c)    
if(s=="+"):
    add()
elif(s=="-"):
    diff()
elif(s=="*"):
    multiply()
elif(s=="%"):
    modulo()
elif(s=="/"):
    div()    



