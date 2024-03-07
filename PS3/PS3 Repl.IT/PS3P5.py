# NOTES :
#'\x1B[4m' → makes text underlined
#'\x1B[1m' → makes text bold
#'\x1B[1;4m' → makes text bold and underlined
#'\x1B[0m' → closing tag

#title
print('\x1B[1m' + "This Program Will Calculate The Area and The Perimeter Of a Circle" + '\x1B[0m')

#input
print("\n")
rad = float(input("Please enter the radius of the circle → "))
print("\n")

#calculations
area = 3.14 * rad * rad
perimeter = 2 * 3.14 * rad

#round
around = "{:,.3f}".format(area)
pround = "{:,.3f}".format(perimeter)

#output
print(" • " + '\x1B[4m' + "The area of the circle is" + '\x1B[0m' + " → " + str(around))
print("\n")
print(" • " + '\x1B[4m' + "The perimeter of the circle is" + '\x1B[0m' + " → " + str(pround))

