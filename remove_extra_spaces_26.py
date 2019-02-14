str1=list(input())
li=[]
i=0
while i<len(str1):
  if str1[i]==" " and str1[i+1]==" ":
    str1.pop(i)
    str1.pop(i)
  i+=1
print("".join(str1))
