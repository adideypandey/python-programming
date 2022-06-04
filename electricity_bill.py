a=int(input("Enter the units : "))
if(a<=200):
    print("Bill is free....")
elif(a>200 and a<900):
    r=5
    b=r*a
    print("Bill is : "+str(b))
else:
    r=10
    b=r*a
    print("Bill is : "+str(b))    
