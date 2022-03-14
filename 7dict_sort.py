print("Dictionary Sorting")
dict1={'Milan':43,'Raju':12,'Renju':90,'Biju':16,'Bibin':210,'Arjun':190}

# sorting of dictionary
print("Sorting of dictionary")
print(sorted(dict1.items()))
print("Ascending order",sorted(dict1.items(),key=lambda x:x[1]))
print("Descending order",sorted(dict1.items(),key=lambda x:x[1],reverse=True))
