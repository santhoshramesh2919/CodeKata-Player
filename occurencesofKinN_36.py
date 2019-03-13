n,k=map(int,input().split())
count=0
for i in str(n):
  if int(i)==k:
    count+=1
print(count)
