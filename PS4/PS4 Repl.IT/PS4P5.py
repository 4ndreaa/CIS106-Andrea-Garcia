#input
print("Enter fixed cost")
fixed = float(input(" → "))
print("Enter price per unit")
price = float(input(" → "))
print("Enter cost per unit")
cost = float(input(" → "))

#program
breakeven = fixed / (price - cost)
rbreakeven = "{:,.2f}" .format(breakeven)

#output
print("\n The break even point is → " + rbreakeven + " units")
print("  Have a nice day ! ☺ ")
