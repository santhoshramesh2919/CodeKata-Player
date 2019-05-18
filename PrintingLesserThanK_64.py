n,k=map(int,input().split())
a=list(map(int,input().split()))
op=[]
for i in a:
  if i<k:
    op.append(i)
op.sort()
print(*op)
