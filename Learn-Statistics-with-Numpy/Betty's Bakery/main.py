import numpy as np
"""
For example, her cupcake recipe calls for:
Flour 	Sugar 	Eggs 	Milk 	Butter
2 cups 	0.75 cups 	2 eggs 	1 cups 	0.5 cups
"""
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
#print(recipes)
#Select all elements from the 3rd column and save them to the variable eggs.
eggs = recipes[:,2]
#print(eggs)

one_egg = recipes[(eggs == 1)]
#print(one_egg)

cookies = recipes[2,:]
double_batch = cupcakes * 2
grocery_list = double_batch + cookies
print(grocery_list)