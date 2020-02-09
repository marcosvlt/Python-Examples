"""

Fibonacchi formula.

"""

number_total = int(input('\nInput the maximum number\n'))

a, b, = 0, 1

while a < number_total:
    print(a, end=',')
    a, b = b, a + b
