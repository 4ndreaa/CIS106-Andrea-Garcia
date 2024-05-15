from FunctionPS10P2 import squareftgeP2

print("Do you want to calculate number of gallons of paint needed for a room?")
answer = input("\x1B[1m(Y/N) → \x1B[0m")
answer = answer.upper()
print("\n")

while answer == "Y":
  len = float(input("◦ Enter the length of the room → " ))
  wid = float(input("◦ Enter the width of the room → "))
  h = float(input("◦ Enter the height of the room → "))
  
  print("\n")
  footage = squareftgeP2(len, wid, h)
  gallons = footage / 50
  print("......................................................")
  print("  You need \x1B[4m", int(gallons) , "\x1B[0m gallons of paint to paint the room.")
  print("     → a gallon of paint covers 50 square feet ←")
  print("......................................................")
  print("\n")
  print("Do you want to calculate number of gallons of paint needed another room?")
  answer = input("\x1B[1m(Y/N) → \x1B[0m")
  answer = answer.upper()
  
  

