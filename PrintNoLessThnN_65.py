n=int(input())
a=list(map(int,input().split()))
op=[]
for i in a:
  if i<n:
    op.append(i)
op.sort()
print(*op)
