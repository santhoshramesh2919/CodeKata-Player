def odd(n):
  if n%2==1:
    return True
  else:
    return False
  
x=int(input())
for i in range(1,x+1):
  if odd(x/i):
    print(i)
    break
