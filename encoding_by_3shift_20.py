str1=list(input())
li1=[]
li2=[]
for i in str1:
  li1.append(ord(i)%64)
for i in range(len(li1)):
  li1[i]+=3
  if li1[i]>26:
    li1[i]-=26
for j in li1:
  li2.append(chr(j+64)) 
print("".join(li2))
