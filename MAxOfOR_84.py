#input
#maximum
    
n=int(input())
li=list(map(int,input().split()))
ans=li[0]
for i in range(1,len(li)):
  ans|=li[i]
print(ans)
