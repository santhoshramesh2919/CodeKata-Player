n,k=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
for i in range(1,k):
  li.pop(0)
print(min(li))
