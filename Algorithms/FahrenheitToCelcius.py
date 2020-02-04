"""
 C = 5*(F - 32.0) / 9.0

"""

F = float(input('Enter the temperature in Farenheit \n'))

C = 5 * (F - 32.0) / 9.0


print(f'{F} Farenheit in Celcius is {round(C, 1)}')
