n=input()
li=[]
for i in n:
  li.append(int(i))
for i in li:
  if li.count(i)>1:
    print("yes")
    break
else:
  print("no") 
