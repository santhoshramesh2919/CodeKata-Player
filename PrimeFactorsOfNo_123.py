def isprime(n):
  if n==2:
    return True
  else:
    for i in range(2,n):
      if n%i==0:
        return False
    else:
      return True

no=int(input())
op=[]
for i in range(2,no):
  if no%i==0 and isprime(i):
    op.append(i)
print(*op)
