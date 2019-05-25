s1,s2=map(str,input().split())
if len(s1)==len(s2):
  print(s1+s2)
else:
  print(s1[:len(s2)]+s2)
