n=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(len(li)):
  if li[i]%2==0:
    op.append(sum(li[:i+1]))
  else:
    op.append(li[i])
print(*op)

