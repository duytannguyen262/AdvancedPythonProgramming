rat_1=[2,5,3,6,3,4,5,7,3,5]
rat_2=[6,4,3,2,3,5,3,4,5,6]

def cauA():
    if rat_1[0] >= rat_2[0]:
        print("Rat 1 weighed more than rat 2 on day 1.")
    else:
        print("Rat 1 weighed less than rat 2 on day 1.")

def cauB():
    if rat_1[0] >= rat_2[0] and rat_1[8] >= rat_2[8]:
         print("Rat 1 remained heaver than Rat 2.")
    else:
         print("Rat 2 became heavier than Rat 1.")
def cauC():
    if rat_1[0] >= rat_2[0]:
        if rat_1[8] >= rat_2[8]:
            print("Rat 1 remained heavier than rat 2.")     
        else:
            print("Rat 2 became heavier than Rat 1.")
    else:
         print("Rat 2 became heavier than Rat 1.")
cauC()