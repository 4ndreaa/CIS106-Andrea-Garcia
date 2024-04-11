#input
print("Enter the quantity of widget")
qty = int(input(" → "))

if qty > 10000:
  price = 10
elif 5000 <= qty <= 10000:
  price = 20
else:
  price = 30

extPrice = float(qty * price) 
tax = extPrice * 0.7
total = tax + extPrice

#round
rextPrice = "{:,.2f}".format(extPrice)
rtax = "{:,.2f}".format(tax)
rtotal = "{:,.2f}".format(total)

#output
print("\n")
print("◦ Extended price is → $", rextPrice)
print("\x1B[4m◦ Tax is → $", rtax, "          \x1B[0m")
print("  • Your total is → $", rtotal)

