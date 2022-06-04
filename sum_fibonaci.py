n=int(input("Enter the range : "))
a=0
b=1
p=a+b
print(a)
print(b)
s=0
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(c)
    s=s+a+p
print("Sum is : "+str(s))    
