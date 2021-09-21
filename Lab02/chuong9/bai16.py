rat_1=[2,5,3,6,3,4,5,7,3,5]
rat_2=[6,4,3,2,3,5,3,4,5,6]

rat_1_weight=rat_1
rat_2_weight=rat_2

def cauA():
    week=1
    while rat_1_weight[week]/rat_1_weight[0] -1 < .25:
        week+=1
    print(week)

def cauB():
    week=0
    while rat_1_weight[week]/rat_2_weight[week] -1 < .10:
        week+=1
    print(week)

cauA()
cauB()