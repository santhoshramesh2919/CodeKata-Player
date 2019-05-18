n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
op=[]
for i in a:
  if i in b and i not in op:
    op.append(i)
print(*op)
