lst="newpythonnew java"
lstnew=[x for x in lst.casefold()]
dict={}.fromkeys(lstnew,0)
for x in lst.casefold():
    if x in dict:
        dict[x]=dict[x]+1
print(lst)
print(dict)