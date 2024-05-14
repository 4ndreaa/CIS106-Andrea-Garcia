print("do you want to run this program? (y/n)")
answer = input()
answer = answer.lower()

employee_count = 0
sum = 0

print("\n")

while answer == "y":
  print("                  Running...")
  print("◦ Enter your last name")
  name = str(input("→ "))
  print("◦ Enter the hours worked")
  hours = float(input("→ "))
  print("◦ Enter your pay rate")
  pay = float(input("→ "))

  print("\n")

  if hours > 40:
    extra = hours - 40
    xtpay = pay * 1.5
    extra = extra * xtpay
    grosspay = (hours * pay) + extra
    rgrosspay = "{:,.2f}".format(grosspay)
    print("Hello, " + name + "!")
    print("Your gross pay is $" + rgrosspay)
    
  else:
    grosspay = hours * pay
    rgrosspay = "{:,.2f}".format(grosspay)
    print("Hello, " + name + "!")
    print("Your gross pay is $" + rgrosspay)

  employee_count = employee_count + 1
  sum = sum + grosspay
  
  
  print("do you want to run this program? (y/n)")
  answer = input("→ ")
  answer = answer.lower()

  print("\n")
  
rsum = "{:,.2f}".format(sum)
print("◦ The number of employees who run this program is → ", employee_count)
print("◦ The sum of all gross pay is $" + rsum)
avrgpay = sum / employee_count
ravrgpay = "{:,.2f}".format(avrgpay)
print("◦ The average pay is $" + ravrgpay)

