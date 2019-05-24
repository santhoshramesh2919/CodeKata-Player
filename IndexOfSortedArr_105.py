n=int(input())
li=list(map(int,input().split()))
re=li
li=sorted(li)
res=[]
for i  in li:
  res.append(re.index(i)+1)
print(*res)
