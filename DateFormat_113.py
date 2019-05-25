li=list(map(int,input().split("/")))
if li[0]<31 and len(str(li[0]))==2 and len(str(li[1]))==2 and li[1]<12 and len(str(li[2]))==4:
  print("yes")
else:
  print("no")
