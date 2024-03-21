#input
print("Enter the number of books you want to purchase")
books = int(input(" → "))
print("Enter the cost per book")
perbook = float(input(" → "))

totalcost = books * perbook
shipping = float()
shipping = 0 if totalcost > 50 else 25
ordertotal = totalcost + shipping

#round
rtotalcost = "{:,.2f}".format(totalcost)
rshipping = "{:,.2f}".format(shipping)
rordertotal = "{:,.2f}".format(ordertotal)

#output
print("\n")
print("◦ The total cost is: $" + str(rtotalcost))
print("◦ The cost of shipping is: $" + str(rshipping))
#having fun
print("_______________________________________________")
print("\n • The total cost of your order is: $" + str(rordertotal))
print("      Thank you for shopping with us!! ♡ ")

