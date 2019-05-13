#power of k
def isPowerOfk(n,k):
    if n==0:
        return False
    while(n!=1):
        if (n%k!=0):
            return False
        n=n//k
    return True

n,k=map(int,input().split(" "))
print("yes" if isPowerOfk(n,k) else "no")
