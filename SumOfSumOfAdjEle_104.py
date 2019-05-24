n=int(input())
li=list(map(int,input().split()))
s=0
for i in range(len(li)-1):
  m=(li[i]+li[i+1])
  s+=m
print(s)
