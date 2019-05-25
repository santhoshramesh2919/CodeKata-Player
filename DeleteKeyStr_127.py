s=list(map(str,input().split()))
k=input()
for i in s:
  if i==k:
    s.pop(s.index(i))
print(*s)
