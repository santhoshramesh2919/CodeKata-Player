#Rotating a string by k
n,m=input().split(" ")
print(n[len(n)-int(m):]+n[:len(n)-int(m)])
