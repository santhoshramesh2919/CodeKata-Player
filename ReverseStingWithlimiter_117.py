s=input()
res=""
for i in range(len(s)-1,0,-1):
  res+=s[i]+"-"
res+=s[0]
print(res)
  
