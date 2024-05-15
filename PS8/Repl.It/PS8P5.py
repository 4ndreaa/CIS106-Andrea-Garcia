#connect to file
with open("Students.txt", "r") as file:
#siempre que se va a contar algo se iguala a 0 para que el programa lo vaya contando ↓
  totaltuition = 0
  count = 0
  print("       \x1B[1;4m    Student Tuition     \x1B[0m")
  print("\n")
#first read has to be outside the loop :
#rstrip("\n") es para q borre la linea
#rstrip() es para q borre
  name = file.readline().rstrip()
#loop as long as the readline is not null
  while name != "":
    dcode = str(file.readline().rstrip())
    costpercredit = 250 if dcode == "I" else 500
    credits = int(file.readline())
    tuition = credits * costpercredit

    print("\x1B[1;4m", name, "\x1B[0m")
    print("◦ Credits taken → ", credits)
    print("◦ Tuition owed →", format(tuition, ".2f"))
    print("\n")
    

    count = count + 1
    totaltuition = totaltuition + tuition
    name = file.readline().rstrip()

  print("...................................")
  print("\x1B[1m Total tuition is → \x1B[0m $", format(totaltuition, ".2f"))
  print("\x1B[1m Total number of students is → \x1B[0m", count)
  print("...................................")
