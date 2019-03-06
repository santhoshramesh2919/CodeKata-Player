s1,s2,k=input().split()
count=0
for i in range(len(s1)):
  if s1[i]!=s2[i]:
    count+=1
if count==int(k):
  print("yes")
else:
  print("no")
