n=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(0,len(li)):
  op.append(sum(li[:i+1]))
res=op
op=sorted(op,reverse=True)
r=[]
for i in range(len(op)):
  r.append(op[i]+res[i])
print(*r)
