def fact(n):
  fac=1
  for i in range(2,n+1):
    fac=fac*i
  return fac


n,k=map(int,input().split())
p=fact(n)//fact(n-k)
print(p)
