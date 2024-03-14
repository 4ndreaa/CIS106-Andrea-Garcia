print("Enter how much did you pay for your meal")
meal = float(input(" → "))
#math
tip15 = meal * 0.15
tip18 = meal * 0.18
tip20 = meal * 0.20
total15 = meal + tip15
total18 = meal + tip18
total20 = meal + tip20
#round
meal_str = "{:.2f}".format(meal)
tip15_str = "{:.2f}".format(tip15)
tip18_str = "{:.2f}".format(tip18)
tip20_str = "{:.2f}".format(tip20)
total15_str = "{:.2f}".format(total15)
total18_str = "{:.2f}".format(total18)
total20_str = "{:.2f}".format(total20)
#output, \n means new line
print("\n")
print("Thank you for choosing us!", "\n Tip is greatly appreciated. ♡")
print("\n")
print("Your meal was → $" + meal_str)
print("with a 15% ( $" + tip15_str + " ) tip, your total is → $" + total15_str)
print("with a 18% ( $" + tip18_str + " ) tip, your total is → $" + total18_str)
print("with a 20% ( $" + tip20_str + " ) tip, your total is → $" + total20_str)

#just having fun :p
print("\n")
print("Enter the percentage you want to tip")
tipchosen = float(input(" → "))
if tipchosen == 15:
  print("your total is → $" + total15_str)
elif tipchosen == 18:
  print("your total is → $" + total18_str)
elif tipchosen == 20:
  print("your total is → $" + total20_str)
else:
  print("invalid tip percentage")