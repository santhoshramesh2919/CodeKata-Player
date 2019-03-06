n,l=map(int,input().split())
count=0
for i in range(n,l):
  p=i**(1/2)
  if p==int(p):
    count+=1
print(count)
