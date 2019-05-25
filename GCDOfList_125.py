from math import gcd
n=int(input())
list1 =list(map(int,input().split()))  
l = list1[0]
for i in list1[1:]:
  l =gcd(l, i)
print(l)
