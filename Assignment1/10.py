def gp(a, r, n):
    for n in range(0, 10):
        result = a * pow(r, n)
        print(result)

a = int(input())
r = int(input())
n = 10
gp(a, r, 10)

