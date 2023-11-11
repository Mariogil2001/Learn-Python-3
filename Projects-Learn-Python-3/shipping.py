"""
Brief: A program that will take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers

Author: Mario Gil Domingo

Date: 16-07-2023

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal's Shippers.
"""
try:
    weight = float(input("Package weight: "))
except EOFError as e:
    print(e)

"""
Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.

Weight of Package 	                    Price per Pound 	      Flat Charge
2 lb or less 	                              $1.50 	              $20.00
Over 2 lb but less than or equal to 6 lb 	  $3.00 	              $20.00
Over 6 lb but less than or equal to 10 lb 	$4.00 	              $20.00
Over 10 lb 	                                $4.75                 $20.00

We need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.
""" 
charge_ground_shipping = 20
if weight <= 2:
  cost_ground = weight * 1.5 + charge_ground_shipping
elif weight <= 6:
  cost_ground = weight * 3.0 + charge_ground_shipping
elif weight <= 10:
  cost_ground = weight * 4.0 + charge_ground_shipping
elif weight > 10:
    cost_ground = weight * 4.75 + charge_ground_shipping
print("Ground Shipping $",cost_ground)
"""
Ground Shipping Premium, which is a much higher flat charge, but you aren't charged for weight.
"""
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)

"""
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Weight of Package 	                      Price per Pound 	Flat Charge
2 lb or less 	                                $4.50         	$0.00
Over 2 lb but less than or equal to 6 lb 	    $9.00         	$0.00
Over 6 lb but less than or equal to 10 lb 	  $12.00        	$0.00
Over 10 lb 	                                  $14.25 	        $0.00
"""
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone = weight * 9.0 
elif weight <= 10:
  cost_drone = weight * 12.0 
elif weight > 10:
    cost_drone = weight * 14.25
print("Drone Shipping $",cost_drone)



  