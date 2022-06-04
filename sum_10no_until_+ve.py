s=0
for i in range(1,11):
    a=int(input("Enter the no. : "))
    if(a>0):
        s=s+a
    elif(a<0):
        break    
print("Sum is : "+str(s))    