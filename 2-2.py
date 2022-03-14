lst=[]
l=int(input("enter the limit\t"))
for i in range(l):
    a=int(input("enter the value\t"))
    lst.append('over' if a>100 else a)
print(lst)
