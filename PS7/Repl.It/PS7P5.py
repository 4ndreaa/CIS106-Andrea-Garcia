print("Do you want to run this program? (y/n)")
answer = str(input("→ "))
answer = answer.lower()

print("\n")
discount_sum = 0
while answer == "y":
  print("                  Running...")
  print("\n")
  print("◦ Enter the quantity you want to buy")
  qty = int(input("→ "))
  print("◦ Enter the price of the item")
  price = float(input("→ "))

  print("\n")
  price = price * qty
  rprice = "{:,.2f}".format(price)
  
  discrate = 0.25 if price < 1000 else 0.10
  
  disc = price * discrate
  rdisc = "{:,.2f}".format(disc)
  total = price - disc
  rtotal = "{:,.2f}".format(total)

  print(" ◦ The extended price is $", rprice)
  print("\x1B[4m ◦ The discount is $", rdisc, "          \x1B[0m")
  print("      The total is $", rtotal)

  print("\n")
  
  discount_sum = discount_sum + disc
  

  print("Do you want to run the program again? (y/n)")
  answer = str(input("→ "))
  answer = answer.lower()
  
rdisc_sum = "{:,.2f}".format(discount_sum)
print("\n")
print("The total discount is $", rdisc_sum)
