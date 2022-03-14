a=int(input("enter the limit\t"))
# a=4
for i in range(1,a):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(a, 0,-1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")