lst1=[2,5,7,8,9,1,2,60,70,20]
lst2=[5,8,9,1,2,3,674,7,8,0,200]
print(lst1,lst2)
lst=[]
for i in lst1:
    if i in lst2:
        lst.append(i)
print("value occurance in both list is:\t",lst)