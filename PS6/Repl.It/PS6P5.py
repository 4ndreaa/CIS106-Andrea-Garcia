#input
print("Enter last name")
name = str(input(" → "))
print("Enter salary")
salary = float(input(" → "))
print("Enter job level")
level = int(input(" → "))

if level >= 10:
  bonus = 0.25
  rate = 25
elif 5 <= level <= 9:
  bonus = 0.20
  rate = 20
else:
  bonus = 0.10
  rate = 10

bonus = bonus * salary

#round
rbonus = "{:,.2f}".format(bonus)

#output
print("\n")
print("Hello " + name + ", you have a bonus rate of " + str(rate) + "%")
print("Your bonus is → $" + str(rbonus))
print("\n  Congratulations!!")
