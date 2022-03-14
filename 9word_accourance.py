words=input("enter the sentance\t")
count={}.fromkeys(words.casefold(),0)
for i in words.casefold().split(' '):
    for j in i:
        count[j]+=1
print(count)