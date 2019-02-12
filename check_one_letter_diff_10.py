str1,str2=map(str,input().split(" "))
count=0
for i in range(0,len(str1)):
  if str1[i]!=str2[i]:
    count+=1
if count==1:
  print("yes")
else:
  print("no")
