#input
print("Enter the type of item (A or B)")
item=str(input(" → "))
print("Enter the quantity")
quantity = int(input(" → "))

if item == "A" or item == "a":
  u_price = 10 
elif item == "B" or item == "b":
  u_price = 20
#having fun :p
else:
  print("Invalid item type")
  exit()

ext_price = u_price * quantity

#round
ru_price = "{:,.2f}".format(u_price)
rext_price = "{:,.2f}".format(ext_price)

#output
print("\n")
print("\x1B[4m Information about your item: \x1B[0m")
print("◦ Item type → '", item, "'")
print("◦ Unit price → $" + str(ru_price))
print("◦ Extended price → $" + str(rext_price))

