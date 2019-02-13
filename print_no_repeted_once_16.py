#print the no that is repeated once
n=int(input())
str1=list(map(int,input().split()))
dic={}
max=0
for i in str1:
  dic[i]=str1.count(i)
for key in dic:
  if dic[key]==1:
    print(key)
    break
  
