
def fib(num):
  a=0
  b=1
  sum=0
  count=1
  lst=[]
  while(count<=num):
    lst.append(sum)
    count+=1
    a=b
    b=sum
    sum=a+b

  return lst



num = int(input("Enter the value of limit \t"))
print("Fibonacci Series: {0}".format(fib(num)))
