n,k=map(int,input().split())
li=list(map(int,input().split()))
res=list(set(li))
op=[]
for i in res:
  if li.count(i)<k:
    op.append(i)
print(*op)
