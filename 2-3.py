l=int(input("enter the num of first names\t"))
counts=0
for i in range(l):
    a=str(input("enter the name\t").split(" ")[0])
    counts+=a.count('a');
print(counts)
