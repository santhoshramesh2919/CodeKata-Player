#print repeated words
str1=input()
dic={}
max=0
for i in str1:
  if i!=" ":
    dic[i]=str1.count(i)
    if dic[i]>max:
      max=dic[i]
for key in dic:
  if dic[key]==max:
    print(key)
    break
  
