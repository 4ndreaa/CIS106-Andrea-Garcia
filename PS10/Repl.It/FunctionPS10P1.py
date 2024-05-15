def sales_forcastP1(m, fc):
  if m == "jan" or m == "feb" or m == "mar":
    fc = fc * 1.1

    #having fun :p
    if m == "jan":
      m = "January"
    elif m == "feb":
      m = "February"
    elif m == "mar":
      m = "March"
      
  elif m == "apr" or m == "may" or m == "jun":
    fc = fc * 1.15

    #having fun :p
    if m == "apr":
      m = "April"
    elif m == "may":
      m = "May"
    elif m == "jun":
      m = "June" 

  elif m == "jul" or m == "aug" or m == "sep":
    fc = fc * 1.2

    #having fun :p
    if m == "jul":
      m = "July"
    elif m == "aug":
      m = "August"
    elif m == "sep":
      m = "September"
      
  elif m == "oct" or m == "nov" or m == "dic":
    fc = fc * 1.25

    #having fun :p
    if m == "oct":
      m = "October"
    elif m == "nov":
      m = "November"
    elif m == "dec":
      m = "December"
      
  else:
      fc = 0
      print("          ***Invalid month***")
  return m, fc
  