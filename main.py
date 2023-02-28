#Calculating the shipping cost for a given weight of package in pounds
def shipping_cost(weight):
cost = weight * 0.10
if weight > 25:
cost += 10
if weight > 50:
cost += 15
if weight > 100:
cost += 30
return cost
