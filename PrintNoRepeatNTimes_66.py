n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in a:
  if a.count(i)==k:
    print(i)
    break
    
