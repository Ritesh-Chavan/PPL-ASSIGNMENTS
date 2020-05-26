import math
arr = []

def divisors(n):
    i = 1
    while (i <= n):
        if n % i == 0 :
            arr.append(i)
        i = i + 1

def harmonic_mean(n):
    arr.clear()
    divisors(n)
    num = len(arr)
    deno = 0
    for i in range(0, len(arr)):
        deno = deno + (n / arr[i])
    deno = deno / n 
    hm = num / deno
    return hm

count = 0
for j in range(1,10000):
    t = harmonic_mean(j)
    if t - int(t) == 0 :
        if count < 10:
            print(j)
            count = count + 1
