n=int(input())
li=[]
for i in range(n):
  li.append(input())
li=sorted(li)
print(li)
li.sort(key=len)
print(li[0])
