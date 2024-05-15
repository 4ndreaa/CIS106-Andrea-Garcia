#agrega un while loop 

print("Enter a principle amount")
principle = input("→ ")
print("Enter a rate of interest(in decimals)")
interest = input("→ ")
print("\n")
print("\n")

total_interest = 0 

#lo que esta en parentesis es: (1,6,1)
#el primer numero (1) es el numero con el que se empieza
#el segundo numero (6) de veces que se repite
#el tercer numero (1) es el increment, es decir, el numero por el cual va a ir sumando


for y in range(1,6,1):
  annual = float(principle) * float(interest)
  ending = float(principle) + float(annual)

  #round
  rprinciple = "{:,.2f}".format(float(principle))
  rending = "{:,.2f}".format(float(ending))
  
  total_interest = total_interest + annual
  
  print("        \x1B[1;4m     Year → ", y, "      \x1B[0m")
  print("◦\x1B[1m Beginning Balance → \x1B[0m ", "$", rprinciple)
  print("◦\x1B[1m Ending Balance → \x1B[0m" , "$", rending)
  print("\n")

 
  
rtotal = "{:,.2f}".format(float(total_interest))
print("...................................")
print("Total interest earned → $" + rtotal)
print("...................................")
  
  