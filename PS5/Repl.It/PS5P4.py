print("\x1B[1;4m      WARRANTY INFORMATION       \x1B[0m")
print("\nThe warrantee of an appliance depends on the cost of the appliance.")
print("Lets see if you qualify for a warrantee")
print("\n")

#input
print("Enter the name of the appliance")
appliance = str(input(" → "))
print("Enter the cost of the appliance")
cost = float(input(" → "))

warrantee = cost * 0.10 if cost > 1000 else cost * 0.05
total = cost + warrantee

#round
rcost = "{:,.2f}".format(cost)
rwarrantee = "{:,.2f}".format(warrantee)
rtotal = "{:,.2f}".format(total)

#output
print("\n")
print("\x1B[4m       Appliance → " + appliance + "       \x1B[0m")
print("◦ Cost of appliance → $" + str(rcost))
print("◦ Warranty cost → $" + str(rwarrantee))
print("◦ Total cost → $" + str(rtotal))