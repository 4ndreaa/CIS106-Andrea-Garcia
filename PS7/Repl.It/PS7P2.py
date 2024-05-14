print("Enter a start value:")
start = int(input("→ "))
print("Enter an increment value:")
inc = int(input("→ "))
print("Enter a stop value:")
end = int(input("→ "))
print("\n")
print("Here are your values:")
print("◦", start)
while start < end:
  start = start + inc
  print("◦", start)

