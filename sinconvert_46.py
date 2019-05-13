import math

n=int(input())
rad=math.radians(n)
val=round(math.sin(rad),1)
if n==90:
    print("1")
    
elif val==0:
    print("0")
else:
    print(val)
