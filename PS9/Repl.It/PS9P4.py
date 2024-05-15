def payrate(code):
  if code == "L":
    prate = 25
  elif code == "A":
    prate = 30
  elif code == "J":
    prate = 50
  else:
    print("Invalid code")
    prate = 0

  return prate

sum = 0

print("Do you want to calculate an employee's pay?")
answer = input("\x1B[1m (Y/N) →  \x1B[0m")
answer = answer.upper()

while answer == "Y":
  print("◦ Enter last name")
  name = str(input("  → "))
  print("◦ Job code")
  code = str(input("  → "))
  code = code.upper()
  print("◦ Hours worked")
  hours = float(input("  → "))

  print("\n")

  rate = payrate(code)

  if hours > 40:
    xtrahours = hours - 40
    overtime = xtrahours * 1.5 * rate
    gross = rate * 40 + overtime
  else:
    gross = hours * rate

  sum = sum + gross

  print("...................................")
  print("◦ Last name → " + name)
  print("◦ Gross pay → $" + format(gross, ".2f"))
  print("...................................")
  
  print("\n")
  print("Do you want to calculate an employee's pay?")
  answer = input("\x1B[1m (Y/N) →  \x1B[0m")
  answer = answer.upper()

print("\n")
print("\x1B[1m Total pay → \x1B[0m$" + format(sum, " .2f"))