#sorting based on length
n=int(input())
li=list(map(str,input().split()))
li2=sorted(li)
print(*sorted(li2,key=len))
