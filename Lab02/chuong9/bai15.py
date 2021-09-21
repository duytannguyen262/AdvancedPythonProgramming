width = 1
def cauA(width):
    while width < 8:
        print('T' * width)
        width += 1
def cauB(width):
    while width < 8:
        print(' ' * ( 7 - width), 'T' * width, sep='')
        width += 1
cauA(width)
cauB(width)
