def fact1(num):
    fact=1
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        for i in range(1,num+1):
            fact=fact*i
        return fact
num=int(input("enter the number\t"))
print("factorial is {0}".format(fact1(num)))