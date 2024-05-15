from FunctionPS10P1 import sales_forcastP1

print("Do you want to run the program?")
answer = input("\x1B[1m(y/n) → \x1B[0m")
answer = answer.lower()

print("\n")
while answer == "y":
  name = input("◦ Enter your last name → ")
  month = input("◦ Enter the sales month \x1B[1m(Jan, Feb, etc) → \x1B[0m")
  month = month.lower()
  sales = float(input("◦ Enter the sales → "))

  print("\n")
  print("...........................................")
  month, forecasted_sales = sales_forcastP1(month,sales)
  print("The forecasted sales for \x1B[4m" +  month + "\x1B[0m are $" + str(format(forecasted_sales, ".2f")))
  print("...........................................")
  print("\n")
  print("Do you want to run the program?")
  answer = input("\x1B[1m(y/n) → \x1B[0m")
  answer = answer.lower()

