#Power of 2
def isPowerOf2(n):
    if n==0:
        return False
    while(n!=1):
        if (n%2!=0):
            return False
        n=n//2
    return True

n=int(input())
print("yes" if isPowerOf2(n) else "no")
