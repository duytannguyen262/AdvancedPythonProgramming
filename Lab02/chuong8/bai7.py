def same_first_last(L):
    if len(L) >= 2:
        return L[0] == L[-1]

print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))
