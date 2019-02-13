#Removing vowels in a string
n=int(input())
str1=list(input())
vo=['a','e','i','o','u']
for i in str1:
  if i in vo:
    str1.pop(str1.index(i))
print("".join(str1))
