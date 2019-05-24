#sum of pdd nos
n,k=map(int,input().split())
s=0
for i in range(n,k+1):
  if i%2==1:
    s+=i
print(s)
