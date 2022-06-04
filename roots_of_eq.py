a=int(input("Enter coefficient of x*x : "))
b=int(input("Enter coefficient of x : "))
c=int(input("Enter constant : "))
d=b*b-4*a*c
D=pow(d,.5)
x1=(-b+D)/(2*a)
x2=(-b-D)/(2*a)
print(x1)
print(x2)