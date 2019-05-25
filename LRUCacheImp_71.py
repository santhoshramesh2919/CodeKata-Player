n,k=map(int,input().split())
li=list(map(int,input().split()))
res=[]
for i in li:
  if len(res)<k:
    res.append(i)
  else:
    for j in range(k-1):
      res[j]=res[j+1]
    res[k-1]=i
print(*res)
