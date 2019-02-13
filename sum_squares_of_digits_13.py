#Sum of squares of digits
n=int(input())
sum1=0
while n!=0:
  r=n%10
  sum1=sum1+r**2
  n=n//10
print(sum1)
