def top_three_avg(grade1, grade2, grade3, grade4):
  total = grade1 + grade2 + grade3 + grade4
  top_three = total - min(grade1, grade2, grade3, grade4)
  return top_three / 3
print(top_three_avg(50, 60, 70, 80))