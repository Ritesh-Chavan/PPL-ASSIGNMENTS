import random

print("Guess a number between 1 to 100:")

t = random.randrange(1, 100,3)
print("Five attempts available:")
for i in range(0, 5):
    x = int(input())
    if x == t:
        print("success")
    else:
        if t > x:
            print("number is greater than entered no.")
        else:
            print("number is smaller than entered no.")
print("The corect no. is", t)

