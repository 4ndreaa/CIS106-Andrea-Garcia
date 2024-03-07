print ("Enter stock symbol you want to buy")
stock = input(" → ")
print ("Enter the number of shares that you want to buy")
shares = float(input(" → "))
print ("Enter the price per share")
cost = float(input(" → $"))
inv = shares * cost

#round it up to 2 decimal places ↓
investround = "{:,.2f}".format(inv)

print("\n")
print ("The amount you invested in ' " + stock + " ' is worth → $" + str(investround)) 



# ** NOTES TO ME → se usa str() frente a la variable investment para que se pueda concatenar con el texto, si no hubiera texto solo se pone 'investment', pero como estas "Sumandolo (+) con un texto (str)" se debe outputear como un string.