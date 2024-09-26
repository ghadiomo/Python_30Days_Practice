from math import sqrt
def divide_or_square(number):
  if number%5==0:
    return f'{sqrt(number):.3f}'
  else:
    return number%5
print(divide_or_square(90))
print(divide_or_square(4))
print(divide_or_square(15))
