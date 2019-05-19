n=int(input())
op=[]
li=list(map(int,input().split()))
for i in range(len(li)-1):
  op.append(max(li[i],li[i+1]))
print(*op)
