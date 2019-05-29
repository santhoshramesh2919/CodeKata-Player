n=input()
s=0
for i in n:
  if int(i)%2==1:
    s+=int(i)
if s%2==0:
  print("E")
else:
  print("O")
