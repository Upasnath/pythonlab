string1=input("enter the string\t")
ch=string1[0]
for c in string1[1:-1]:
    if c==ch:
        b=string1.replace(c,'$')
print(ch+b[1:])