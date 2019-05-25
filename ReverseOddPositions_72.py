li=list(map(str,input().split()))
for i in range(len(li)):
  if i%2==0:
    li[i]=li[i][::-1]
print(*li)
