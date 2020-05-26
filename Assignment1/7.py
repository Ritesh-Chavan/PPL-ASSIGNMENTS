import math

arr = []

def digits(n):
    count = 0
    while( n != 0 ):
        n = n // 10
        count = count + 1
    return count


def armst(k):
    l = k
    p = digits(k)
    sum = 0
    i = 0
    while(i < p):
        r = k % 10 
        k = k // 10
        sum = sum + math.pow(r,p)
        i = i + 1
    if sum == l:
        arr.append(l)

n1 = int(input())
n2 = int(input())
for i in range(n1, n2): 
    armst(i)

    
print(arr)
