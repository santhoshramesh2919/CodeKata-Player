n=int(input())
li=list(map(int,input().split()))
op=[]
ind=0
for i in range(len(li)):
  if li[i]==0:
    op+=li[ind:i]
    ind=i+1
print(*op)
    
  
