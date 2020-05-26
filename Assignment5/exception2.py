
#ZeroDivisionError
a , b = int(input()), int(input())
try:
    if b == 0:
        raise ZeroDivisionError

except ZeroDivisionError as e:
    print('You just divided by zero', e)

else:
    print('a/b =', a/b)


#AssertionError
try:
    a = 100
    b = "ritesh"
    assert a == b
except AssertionError as e:
    print('Wrong Happened',e)


#OverFlowError
try:
    import math
    print(math.exp(1000))

except OverflowError as e:
    print('Something went wrong...', e)


#NameError
try:
    print(ans)

except NameError as e:
    print('ans not found',e)



#TypeError
try:
    print('10' + 10)

except TypeError as e:
    print('You tried adding two incompatible things', e)





