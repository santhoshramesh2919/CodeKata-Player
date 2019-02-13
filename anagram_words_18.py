#anagram
n=int(input())
li=[]
count=0
for i in range(n):
  li.append("".join(sorted(input())))
str1="".join(sorted("kabali"))
for i in li:
  if i==str1:
    count+=1
print(count)
