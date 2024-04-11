#input
print("Enter amount of concert tickets")
qty = int(input(" → "))

if qty >= 25:
  price = 50
elif 10 <= qty <= 24:
  price = 60
elif 5 <= qty <= 9:
  price = 70
else:
  price = 75

totalcost = qty * price

#round
rprice = "{:,.2f}".format(price)
rtotalcost = "{:,.2f}".format(totalcost)

#output
print("\n")
print("◦ Number of tickets → " + str(qty))
print("\x1B[4m◦ The price per ticket is → $" + str(rprice) + "\x1B[0m")
print("• The total cost is → $" + str(rtotalcost))

