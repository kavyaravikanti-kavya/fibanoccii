n=int(input("enter a number= "))
a=0
b=1
sum=0
count=0
while count<n:
  print(sum)
  a=b
  b=sum
  sum=a+b
  count+=1
