from math import gcd
n=int(input())
list1 =list(map(int,input().split()))  
lcm = list1[0]
for i in list1[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
