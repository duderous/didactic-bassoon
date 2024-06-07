#Sal's Shipping
#Ben Engel

#Shipping weight in lbs
weight = 41.5

#Ground Shipping
cost_ground = ""
cost_premium_ground = 125

#Drone Shipping
drone_shipping = ""

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

#Drone Shipping
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9
elif weight > 6 and weight <= 10:
  drone_shipping = weight * 12
elif weight > 10:
  drone_shipping = weight * 14.75

#Print Results in USD
print("Ground Shipping Cost: ${:.2f}".format(cost_ground))
print("Ground Shipping Premium Cost: ${:.2f}".format(cost_premium_ground))
print("Drone Shipping Cost: ${:.2f}".format(drone_shipping))