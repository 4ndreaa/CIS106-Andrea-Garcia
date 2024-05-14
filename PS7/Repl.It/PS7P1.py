print("\x1B[1;4m      Odd numbers from 1 to 25:       \x1B[0m \n")
print("\x1B[1m        ( Using while loop )      \x1B[0m \n")

start = 1
stop = 25
while start<=stop:
  odd=start % 2 
  if odd!=0:
    print("◦", (start))
  start = start + 1