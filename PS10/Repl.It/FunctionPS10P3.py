def discountP3(q, p, d):
  total = float(q) * float(p)
  dp = float(p) * float(d)
  dt = float(total) - float(dp)

  return (dp, dt)
