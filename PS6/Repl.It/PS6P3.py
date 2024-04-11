#input
print("Enter a principle amount of a CD")
principle = float(input(" → "))
print("Enter the year to maturity of CD")
maturity = int(input(" → "))

if principle > 100000 and maturity == 5:
  interest = 0.06
  rate = 6

elif 50000 <= principle <= 100000 and maturity == 10:
  interest = 0.05
  rate = 5

elif 50000 <= principle <= 100000 and maturity == 5:
  interest = 0.04
  rate = 4

else:
  interest = 0.02
  rate = 2

firstyear = principle * interest

#round
rprinciple = "{:,.2f}".format(principle)
rfirstyear = "{:,.2f}".format(firstyear)

#output
print("\n")
print("◦ Principle → $" + str(rprinciple))
print("◦ Interest Rate → " + str(rate) + "%")
print("• First Year Interest → $" + str(rfirstyear))