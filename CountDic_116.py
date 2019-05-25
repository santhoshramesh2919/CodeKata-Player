n=int(input())
li=list(map(int,input().split()))
dic={}
for i in li:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1
li=[]
for i in sorted(dic.items(),key=lambda kv: (kv[1],kv[0]),reverse=True):
  li.append(i[0])
print(*li)
