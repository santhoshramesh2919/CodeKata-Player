
def sides(a,b,c):
    if a!=0 and b!=0 and c!=0:
        if a+b+c==180:
            return True
    return False

p,q,r=map(int,input().split())
if(sides(p,q,r)):
    print("yes")
else:
    print("no")
