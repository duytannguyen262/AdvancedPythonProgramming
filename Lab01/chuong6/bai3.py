import doctest

def average(num1: float, num2: float):
    return (num1 + num2) / 2

print(average(10,20))
print(average(2.5, 3.0))
print(doctest.testmod())
