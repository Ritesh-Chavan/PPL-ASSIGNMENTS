list = []

tp = int(input())
while tp != -1:
    list.append(tp)
    tp = int(input())

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
t = len(list)

for i in range(1,25):
    j = 0
    while j < t:
        if i == list[j]:
            arr[i] = 1
        j = j +1

for k in range(1,25):
    if arr[k] == 0:
        print(k, end = " " )
print("\n")


