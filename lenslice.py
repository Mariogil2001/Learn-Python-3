"""
Brief: You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

Author: Mario Gil Domingo

Date: 17-07-2023
"""
"""
1. To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
"pepperoni" "pineapple" "cheese" "sausage" "olives" "anchovies" "mushrooms"
"""
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
"""
2. To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
 2 6 1 3 2 7 2
"""
prices = [2,6,1,3,2,7,2]
"""
3. Your boss wants you to do some research on $2 slices.
Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.
"""
num_two_dollar_slices = prices.count(2)
"""
4. Find the length of the toppings list and store it in a variable called num_pizzas 
"""
num_pizzas = len(toppings)
"""
5. Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas
"""
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
"""
6.Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.

Each sublist in pizza_and_prices should have one pizza topping and an associated price.
Price 	        Topping
2 	          "pepperoni"
6             "pineapple"
1 	            "cheese"
3 	           "sausage"
2             	"olives"
7 	           "anchovies"
2 	          "mushrooms"
"""
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
"""
8. Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending)
"""
pizza_and_prices.sort()
print(pizza_and_prices)
"""
9. Store the first element of pizza_and_prices in a variable called cheapest_pizza
"""
cheapest_pizza = pizza_and_prices[0][1]
print("The cheapest pizza is the " + str(cheapest_pizza)+ " one!")
"""
10. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza
"""
priciest_pizza = pizza_and_prices[-1][-1]
print ("The priciest pizza is the " + str(priciest_pizza)+ " one!")
"""
11. It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice. 
"""
pizza_and_prices.pop()
"""
12. Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

[2.5, "peppers"]

Add the new peppers pizza topping to our list pizza_and_prices. 
"""
pizza_and_prices.insert(4,[2.5, "peppers"])
"""
13. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
"""
three_cheapest = pizza_and_prices[:3]
"""
14. Great job! The mice are very pleased and will be leaving you a 5-star review. 
"""
print(three_cheapest)
