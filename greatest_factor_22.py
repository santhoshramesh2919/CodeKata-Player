n,k=map(int,input().split())
i=2
li=[]
for i in range(1,max(n,k)+1):
  if n%i==0 and k%i==0:
    li.append(i)
print(max(li))
