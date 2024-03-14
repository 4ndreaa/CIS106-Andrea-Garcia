#input
print("Enter the first exam score")
exam1 = int(input(" → "))
print("Enter the second exam score")
exam2 = int(input(" → "))

fstscore = (exam1 * 0.6)
scndscore = (exam2 * 0.4)
fscore = int(fstscore + scndscore)

#output
print("\n The final score is → "+ str(fscore))

#having fun
print("\n")
if fscore<60:
  print("You failed ")

elif 100>fscore>=60:
  print("\x1B[4m Congratulations!! \x1B[0m You passed ☺")

else:
  print("You have entered a wrong score")
