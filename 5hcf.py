num1=int(input("enter the 1st number\n"))
num2=int(input("enter the 2nd number\n"))
key=num1 if num1<num2 else num2
hcf=1
for i in reversed(range(1,key)):
    if num1%i==0 and num2%i==0:
        hcf=i
        break
print(f" The hcf of the numbers {num1} and {num2} is {hcf}")