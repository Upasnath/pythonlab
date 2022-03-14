word=input("enter the word\t")
count = {}.fromkeys(['a','e','i','o','u'], 0)
for c in word.casefold():
        if c in count:
            count[c] += 1 
print(count)