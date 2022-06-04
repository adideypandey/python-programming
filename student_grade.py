p=int(input("Enter physics marks : "))
c=int(input("Enter chemistry marks : "))
m=int(input("Enter maths marks : "))
per=(p+c+m)/3
if(per>90):
    print("Grade A ")
elif(per>60 and per<90):
    print("Grade B ")    
else:
    print("FAIL")