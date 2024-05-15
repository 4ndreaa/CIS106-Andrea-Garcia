def compute_total_and_taxP5(qty, unit_price):
  global total, tax
  total = qty * unit_price
  tax = total * 0.07
  return tax, total