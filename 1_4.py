myinput=input("enter the message\t")
mylist =list(myinput)
mylist = [ord(character) + 1 for character in mylist]
print(mylist)