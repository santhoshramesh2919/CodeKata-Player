n=int(input())
li=list(map(int,input().split()))
c=1
for i in range(len(li)-1):
  for j in range(i,len(li)):
    c+=1
print(c)
