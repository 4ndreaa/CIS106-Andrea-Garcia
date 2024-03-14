#input
print("Enter the purchase price per share")
pshare = float(input(" → "))
print("Enter the current stock price")
cprice = float(input(" → "))
print("Enter the quantity of stock")
stock = float(input(" → "))

#program
value = float((cprice - pshare) * stock)
rvalue = "{:,.2f}".format(value)

#output
print("\n The value of the stock is → " + str(rvalue))

#having fun
print("\n")
if value < 0:
  print("You are losing money. You should sell your stock.")
elif value > 0:
  print("You are making money. Congrats!")
else:
  print("You are breaking even. Good job!")
      