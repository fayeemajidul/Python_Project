def ground_shipping(weight):
  cost = 0
  if weight <= 2:
    (cost += 1.50);
  return(cost)

print(ground_shipping(1))