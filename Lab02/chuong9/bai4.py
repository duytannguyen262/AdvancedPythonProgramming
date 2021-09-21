#CauA
alkaline_earth_metals=[[4,9.012],[12, 24.305],[20, 40.078],[38, 87.62],[56, 137.327],[88,226]]

def cauA():
    for inner_list in alkaline_earth_metals:
        print(inner_list[0])
        print(inner_list[1])

#CauB
def cauB():
    for inner_list in alkaline_earth_metals:
        print('Atomic number:',inner_list[0])
        print('Atomic weight:',inner_list[1])

#CauC
def cauC():
    number_and_weight = []
    for i in alkaline_earth_metals:
        for j in i:
            number_and_weight.append(j)
    print(number_and_weight)

cauC()