a=int(input("enter the 1st number\n"))
b=int(input("enter the 2nd number\n"))
c=int(input("enter the 3rd number\n"))

if(a>b and a>c):
    print(f"{a} is greater\n")
elif(b>c):
    print(f"{b} is greater\n")
else:
    print(f"{c} is greater")
