from FunctionPS10P3 import discountP3

print("Do you want to calculate the discounted price of an item?")
answer = input("\x1B[1m(y/n) → \x1B[0m")
answer = answer.lower()
print("\n")

while answer == "y":
  qty = input("◦ Enter the quantity → ")
  price = float(input("◦ Enter the price → "))
  disc = float(input("◦ Enter the discount rate in decimal → "))
  #call function
  #cuando llames la funcion debes poner el orden de las variables correctamente
  #las variables que declaras no se pueden llamar igual que las variables que estan en lafuncion
  discount_amount, final_price = discountP3(qty, price, disc)
  #print value returned from function
  print("\n")
  print("...................................")
  print("        Quantity → ", qty)
  print("        Price → ", format(price, ".2f"))
  print("        Discount → $", format(discount_amount, ".2f"))
  print("...................................")
  print("\x1B[1m  The final price is\x1B[0m → $", format(final_price, ".2f"))
  

  print("\n")
  print("Do you want to calculate the discounted price of another item?")
  answer = input("\x1B[1m(y/n) → \x1B[0m")
  answer = answer.lower()