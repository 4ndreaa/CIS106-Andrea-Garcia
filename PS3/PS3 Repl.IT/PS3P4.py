#input info
print("Enter your car's make ")
make = str(input("  → "))
print("Enter your car's model")
model = str(input("  → "))
print("Enter msrp amount")
msrp = float(input("  → "))
print("Enter your car's discount percent in decimals")
dpercent = float(input("  → "))

# Calculations
amountoff = msrp * dpercent
finalprice = msrp - amountoff
percentage = dpercent * 100

#round
msrpround = "{:,.2f}".format(msrp)
amountoffround = "{:,.2f}".format(amountoff)
finalpriceround = "{:,.2f}".format(finalprice)
percentageround = "{:,.0f}".format(percentage)

#output info
print("\n")
print("• Your car's make is → " + make)
print("• Your car's model is → " + model)
print("• Your car's msrp is → $" + str(msrpround))
print("• Your car's discount percent is → " + str(percentageround) + "%")
print("• The amount off is → $ " + str(amountoffround))
print("\n The total price is → $ " + str(finalpriceround))
