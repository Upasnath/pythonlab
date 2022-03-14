color1 = ["White", "Black", "Red"]
color2 = ["Red", "Green"]
print("Colour list is")
print(color1)
print(color2)
print("colours not in 2nd list is:\t")
for element in color1:
    if element not in color2:
        print(element)