#input
print("Enter your last name")
name = str(input(" → "))
print("Enter the number of dependents")
dependents = int(input( " → "))
print("Enter your gross income")
g_income = float(input(" → "))

adj_income = g_income - (dependents * 12000)
taxrate = float()
taxrate = adj_income * 0.2 if adj_income > 50000 else adj_income * 0.1
income_tax = taxrate * adj_income

#round
rg_income = "{:,.2f}".format(g_income)
radj_income = "{:,.2f}".format(adj_income)
rincome_tax = "{:,.2f}".format(income_tax)

#output
print("\n")
print("\x1B[1;4m      ", name, "       \x1B[0m")
print("◦ Gross income → $", rg_income)
print("◦ Number of dependents → ", dependents)
print("◦ Adjusted gross income → $", radj_income)
print("◦ Income tax → $", rincome_tax)