s=list(input())
for i in range(len(s)):
  if s[i].isupper():
    s[i]=s[i].lower()
  elif s[i].islower():
    s[i]=s[i].upper()
print("".join(s))
