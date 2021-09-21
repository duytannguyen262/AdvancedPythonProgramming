values = [[4,9.012],[12, 24.305],[20, 40.078],[38, 87.62],[56, 137.327],[88,226]]

def mystery_function(values):
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)
    return result

mystery_function(values)