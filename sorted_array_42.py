n=int(input())
li=list(map(int,input().split()))
re=li
if sorted(re)==li:
    print("yes")
else:
    print("no")
