#input
print("Enter part number")
part = input(" → ")
print("Enter quantity")
qty = input(" → ")

if part == "10" or part == "55":
  cost = 1.00

elif part == "99":
  cost = 2.00

elif part == "80" or part == "70":
  cost = 3.00

else:
  cost = 5.00

totalcost = float(qty) * float(cost)

#round
rcost = "{:,.2f}".format(cost)
rtotalcost = "{:,.2f}".format(totalcost)

#output
print("\n")
print("◦ Part number → " + str(part))
print("\x1B[4m◦ Cost → $" + str(rcost) + "          \x1B[0m")
print("• Total cost → $", rtotalcost)