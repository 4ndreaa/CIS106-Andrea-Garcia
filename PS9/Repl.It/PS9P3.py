def mpg(miles, gallons):
  mpg = float(miles) / float(gallons)
  return mpg

print("Do you want to know your car's mpg?")
answer = input("\x1B[1m(y/n) → \x1B[0m")
answer = answer.lower()
count = 0

while answer == "y":
  print("\n")
  print("        RUNNING.... ")
  print("\n")
  print("◦ Enter the destination city")
  dest = str(input("  → "))
  print("◦ Enter the distance in miles")
  dist = float(input("  → "))
  print("◦ Enter the gallons used for the trip")
  gal = float(input("  → "))

  milespg = mpg(dist, gal)

  #round
  rmpg = "{:.2f}".format(milespg)
  
  print("\n")
  print("...................................")
  print("The MPG for the trip to \x1B[4m" + dest + "\x1B[0m is " + str(rmpg))
  print("...................................")
  count += 1

  print("\n")
  print("Do you want to know your car's mpg?")
  answer = input("\x1B[1m(y/n) → \x1B[0m")
  answer = answer.lower()
print("\n")
print("\x1B[1m The total of cars calculated is → \x1B[0m", count)

