#
n=int(input())
li=list(map(str,input().split()))
li2=sorted(li,key=len)
print(*li2)
