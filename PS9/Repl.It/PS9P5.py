def calc_tuition(hours,code):
  if code == "I":
    tuition = 250 * float(hours)
  elif code == "O":
    tuition = 550 * float(hours)
  else:
    tuition = 0

  return tuition
    
print("Do you want to calculate tuition?")
answer = input("\x1B[1m(y/n) → \x1B[0m")
answer = answer.upper()

sum = 0

while answer == "Y":
  print("◦ Enter student's last name:")
  name = input("  → ")
  print("◦ Enter student's credit hours:")
  credits = input("  → ")
  print("◦ Enter district code:")
  district = input("  → ")
  district = district.upper()

  print("\n")
  print("...........................")
  tuition =   calc_tuition(credits,district)
  print("\x1B[4mStudent's name\x1B[0m → " + name)
  print("\x1B[4mTuition owed\x1B[0m → $" + format(tuition, ".2f"))
  print("...........................")

  print("\n")
  print("Do you want to calculate tuition?")
  answer = input("\x1B[1m(y/n) → \x1B[0m")
  answer = answer.upper()

  sum = sum + tuition
  
print("\n")
print("  \x1B[1mThe total of all tuition owed is\x1B[0m → $" + format(sum, ".2f"))

