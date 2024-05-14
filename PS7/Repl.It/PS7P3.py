print("Do you want to run this program? (y/n)")
answer = input()
answer = answer.lower()

student_count = 0

while answer == "y":
  print("\n")
  print("                  Running...")
  print("\n")
  print("◦ Enter your last name")
  name = input("→ ")
  print("◦ Enter the first exam score")
  fexam = int(input("→ "))
  print("◦ Enter the second exam score")
  sexam = int(input("→ "))
  
  avgscore = (fexam + sexam) / 2
  ravgscore = "{:,.2f}".format(avgscore)
  student_count = student_count + 1

  print("\n")
  print("Hello, " + name + "!")
  print("Your average score is → " + str(ravgscore))
  
  print("\n")
  print("Do you want to run this program? (y/n)")
  answer = input()
  answer = answer.lower()
  
print("\n")
print("Thank you for using this program!")
print("  → " + str(student_count)  + " students ran this program.")