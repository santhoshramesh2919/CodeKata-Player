s=input()
s=s.lower()
dic={}
li=[]
for i in s:
  if i!=" ":
    dic[i]=s.count(i)
for i in dic:
  if dic[i]==1 :
    li.append(i)
print(*li)
