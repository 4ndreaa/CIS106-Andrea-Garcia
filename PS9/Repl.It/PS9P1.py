def CompExtPrice (qty, price):
  extprice = qty * price
  if extprice > 10000.00:
    discount = extprice * 0.10
    extprice = extprice - discount
  else:
    discount = 0.00
  return extprice

eprice = 0
print("Do you want to calculate the extended price? (y or n)")
loop = input(" → ")
loop = loop.lower()
while loop == "y":
  print("◦ Enter the quantity of the item")
  quantity = float(input("  → "))
  print("◦ Enter the price of the item")
  price_ = float(input("  → "))
  eprice = eprice + CompExtPrice(quantity, price_)
  
  print("...................................")
  print("\x1B[1m The extended price is → \x1B[0m $", format(eprice,".2f"))
  print("\n")
  
  print("Do you want to calculate the extended price again? (y or n)")
  loop = input("→ ")
  loop=loop.lower()
  


