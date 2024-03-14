#input
print("Enter your first name")
name = str(input(" → "))
print("Enter the steps walked today")
steps = int(input(" → "))

#program
cal = int(steps * 0.25)

#output
print("\n")
print("\x1b[1m" + name, "\x1b[0m : you have burned ", cal, " calories today.")

#having fun
print("\n")
if steps >= 10000:
  print(" \x1B[4m You are doing great! \x1B[0m")
else: 
  print("It is recommended that you walk at least 10,000 steps a day.")
  print("\n \x1B[4m You can do it! \x1B[0m")
  