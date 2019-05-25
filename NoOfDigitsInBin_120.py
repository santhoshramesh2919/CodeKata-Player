#Noof digits in bin
n=int(input())
print(len(bin(n).replace("0b","")))
