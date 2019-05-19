n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(len(li)-1):
  for j in range(i+1,len(li)):
    if li[i]<li[j]:
      c+=1
print(c)
