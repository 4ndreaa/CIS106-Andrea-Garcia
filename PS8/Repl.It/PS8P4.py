with open("Inventory.txt", "r") as file:
  sum = 0
  count = 0
  average = 0

  item = file.readline().rstrip()

  print("       \x1B[1;4m     Bakery Inventory     \x1B[0m")
  print("\n")

  while item != "":
    qty = int(file.readline().rstrip())
    price = float(file.readline().rstrip())
    extprice = qty * price
    print("\x1B[1;4m Item → ", item, "\x1B[0m")
    print("◦ Quantity → ", qty)
    print("◦ Extended price →", format(extprice, ".2f"))
    print("\n")
    sum = sum + extprice
    count = count + 1
    average = sum / count
    item = file.readline().rstrip()
    
print("...................................")
print("\x1B[1m Sum of extended prices → \x1B[0m $", format(sum, ".2f"))
print("\x1B[1m Number of orders → \x1B[0m $", format(count, ".2f"))
print("\x1B[1m Average order → \x1B[0m $", format(average, ".2f"))
print("...................................")
