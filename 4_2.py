lst1=[2,5,7,8,9,1,2,3]
lst2=[5,8,9,1,2,3,4,7,8,0,2]
print(lst1,lst2)
if sum(lst1)==sum(lst2):
    print("sum is same")
else:
    print("sum is not same")
print("sum is list1 {0} and sum of list 2 is{1}".format(sum(lst1),sum(lst2)))