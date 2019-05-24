n=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(0,len(li)):
  op.append(sum(li[:i+1]))
print(*op)
