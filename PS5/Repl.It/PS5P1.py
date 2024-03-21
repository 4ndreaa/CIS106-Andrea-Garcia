
#input
print("Enter item quantity")
quantity = int(input("→ "))

unit_price = 3 if quantity >= 1000 else 5

extprice = quantity * unit_price
tax = extprice * 0.07
total = extprice + tax

#round
rtax = "{:,.2f}".format(tax)
rtotal = "{:,.2f}".format(total)
runitprice = "{:,.2f}".format(unit_price)
rextprice = "{:,.2f}".format(extprice)

#output
print("\n")
print("◦ Quantity → " + str(quantity) + "\n◦ Unit Price → $" + str(runitprice))
print("◦ Extended Price → $" + str(rextprice) + "\n◦ Tax → $" + str(rtax))
print("\n")
print("• Your total is → $" + str(rtotal))