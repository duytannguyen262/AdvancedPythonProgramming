fruit = "pineapple"

def cauA():
    pCount = fruit.count('p')
    print(fruit.find('p', pCount))

def cauB():
    upperCase = fruit.upper()
    swapCase = upperCase.swapcase()
    print(fruit.count(swapCase))

def cauC():
    swapCase = fruit.swapcase()
    lowerCase = fruit.lower()
    print(fruit.replace(swapCase, lowerCase))

cauA()
cauB()
cauC()