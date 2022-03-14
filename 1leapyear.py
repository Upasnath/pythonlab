start_yr=int(input("Enter the starting year"))
limit_yr=int(input("Enter the limit year\n"))

lst=[]

for i in range(start_yr,limit_yr):
    if((i%4==0 and i%100!=0) or i%400==0):
        lst.append(i)

print("leap year",lst)
