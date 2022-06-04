a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
c=input("Enter the operator")
if(c=="+"):
    d=a+b
    print(d)
elif(c=="-"):
    if(a>b):
        d=a-b
        print(d)
    elif(a<b):
        d=b-a
        print(d)
    else:
        print("Differenece is 0.")    
elif(c=="*"):
    d=a*b
    print(d)
elif(c=="/"):
    d=a/b
else:
    print("NO operator find...4")        



