print("Thank you for completing the job !! ☺ \n Please enter the amount received from the client")
payment = float(input("  → $"))
amount = payment / 3
roundamount = "{:,.2f}".format(amount)
print("Each person will receive → $" + str(roundamount))
