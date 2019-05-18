def Check(li):
  for i in range(len(li)):
    for j in range(len(li)):
      if i==j:
        continue
      if li[i]+li[j]==x:
        return True
  else:
    return False

n,x=map(int,input().split())
lis=list(map(int,input().split()))
if (Check(lis)):
  print("yes")
else:
  print("no")
