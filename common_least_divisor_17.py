#Common least divisor
l,r=map(int,input().split())
n=max(l,r)
while(1):
  if n%l==0 and n%r==0:
    print(n)
    break
  n+=1
