def BattingAve (hits, bats):
  ave = hits / bats
  return ave

count = 0

for player in range(0,9,1):
  print("◦ Enter the players last name")
  player = str(input("→ "))
  print("◦ Enter the number of hits")
  hits = int(input("→ "))
  print("◦ Enter the number of at bats")
  atbats = int(input("→ "))

  print("...................................")
  average = BattingAve(hits, atbats)
  print(" The batting average for \x1B[4m", player, "\x1B[0m is → ", "{:.3f}".format(average))
  print("...................................")
  print("\n")
  
  count = count + 1
print("      \x1B[1;4m Total of players entered → \x1B[0m", count)

