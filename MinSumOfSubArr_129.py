n=int(input())
li=list(map(int,input().split()))
m=0
if len(li)==1:
  m=li[0]
else:
  for i in range(len(li)-1):
    for j in range(i+1,len(li)):
      s=sum(li[i:j+1])
      if m>s:
        m=s
print(m)
