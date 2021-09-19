def total_occurrences(s1, s2, ch):  
  return s1.count(ch) + s2.count(ch)
print(total_occurrences('color', 'yellow', 'l'))
print(total_occurrences('red', 'blue', 'l'))
print(total_occurrences('green', 'purple', 'b'))