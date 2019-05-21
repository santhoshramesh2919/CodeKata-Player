n,m=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
op=[]
op=li1+li2
op.sort()
print(*op)
