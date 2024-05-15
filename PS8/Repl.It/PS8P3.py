with open("Employees.txt", "r") as file:
  
  sum = 0
  name = file.readline().rstrip()

  print("        \x1B[1;4m     Bonuses and Earnings     \x1B[0m")
  print("\n")
  
  while name != "":
    salary = float(file.readline().rstrip())
    if salary >=100000:
      bonus = salary * 0.20
      rate = 20
    elif salary >=50000:
      bonus = salary * 0.15
      rate = 15
    else:
      bonus = salary * 0.10
      rate = 10
  
    print("◦ ",name, "earned $", format(salary, ".2f"))
    print("      → had a bonus of $", format(bonus, ".2f"))
    sum = sum + bonus
    name = file.readline().rstrip()

  rsum = "{:,.2f}".format(sum)
  print("\n")
  print("...................................")
  print("The total bonus amount is $", format(sum, ".2f"))
  print("...................................")
  
    

  