from typing import List

negatives=([1,2,3,-3,6,-1,-3,1])
def remove_neg(negatives):
    index = 0
    while index < len(negatives):
        if negatives[index] < 0:
            del negatives[index]
        else:
            index+=1
remove_neg(negatives)
print(negatives)