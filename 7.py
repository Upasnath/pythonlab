lst=['hello','world','python','java','newpython','jupyter']
a=0
print(lst)
for x in lst:
    a= len(x) if len(x)>a else a
print(a)
