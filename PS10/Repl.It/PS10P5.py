from FunctionPS10P5 import compute_total_and_taxP5

total = float
tax = float

print("       \x1B[1;4m    Item Total and Tax     \x1B[0m")

# input quantity and unit price from user
qty = int(input("\nEnter item quantity → "))
unit_price = float(input("Enter unit price  → $"))
print("\n")


# Compute total and tax
tax, total = compute_total_and_taxP5(qty, unit_price)

# Display total and tax
print(".......................................")
print("        ◦ Total → $", format(total,".2f"))
print("        ◦ Tax (7%) → $", format(tax,".2f"))
print(".......................................")

