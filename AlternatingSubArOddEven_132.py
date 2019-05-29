n=input()
op=[]
for i in range(len(n)-1):
  c=1
  for j in range(i+1,len(n)):
    if ((int(n[j-1]))%2==0 and (int(n[j]))%2==1) or ((int(n[j-1]))%2==1 and (int(n[j]))%2==0):
      c+=1
  op.append(c)
print(max(op))
