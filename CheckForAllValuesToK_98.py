n,k=map(str,input().split())
f=0
for i in range(int(k)+1):
  if str(i) in n:
    f=1
  else:
    f=0
    break
if f==1:
  print("yes")
else:
  print("no")
