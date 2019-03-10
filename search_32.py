n,k=map(int,input().split())
li=list(map(int,input().split()))
for i in li:
  if i==k:
    print("yes")
    break
else:
  print("no")
