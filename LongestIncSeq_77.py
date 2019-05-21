n=int(input())
li=list(map(int,input().split()))
m=0
for i in range(len(li)-1):
  c=1
  for j in range(i+1,len(li)):
    if li[j]>li[j-1]:
      c+=1
    else:
      break
  if c>m:
    m=c
print(m)
