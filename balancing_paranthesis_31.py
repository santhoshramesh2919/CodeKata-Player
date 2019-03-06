s=input()
stack=[]
flag=0
for i in range(len(s)):
  if s[i]=="(":
    stack.append(s[i])
  elif s[i]==")":
    if len(stack)>0 and stack[len(stack)-1]=="(":
      stack.pop()
    elif len(stack)==0:
      flag=1
if flag==0:
  print("yes")
else:
  print("no")
