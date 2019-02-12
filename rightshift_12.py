n,k=map(int,input().split())
li=list(map(int,input().split()))
li2=sorted(li[-1:-k-1:-1])
for i in range(0,len(li)-k):
  li2.append(li[i])
print(li2)
