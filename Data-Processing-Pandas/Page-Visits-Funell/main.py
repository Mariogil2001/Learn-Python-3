"""
Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:

    1. A user visits CoolTShirts.com
    2. A user adds a t-shirt to their cart
    3. A user clicks “checkout”
    4. A user actually purchases a t-shirt

"""
import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

#Combine visits and cart using a left merge.
visits_cart_left = pd.merge(visits,cart, how = 'left')
#print(visits_cart_left)

#How long is your merged DataFrame?
#print(len(visits_cart_left))

#How many of the timestamps are null for the column cart_time?
null_count = visits_cart_left[visits_cart_left.cart_time.isnull()].count()
#print(null_count)

#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
percent_no_shirt_cart = (null_count/float(len(visits_cart_left))) * 100 # 82.6%
#print(percent_no_shirt_cart)

#What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout_left = pd.merge(cart, checkout, how='left')
null_count_ccl = cart_checkout_left[cart_checkout_left.checkout_time.isnull()].count()
percent_no_proceed_checkout = (null_count_ccl/float(len(cart_checkout_left))) * 100 #25.31%
#print(percent_no_proceed_checkout)

#Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
#print(all_data)

#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
all_data['count_num'] = all_data['checkout_time'].isnull()
number = all_data[all_data['count_num'] == False].count()
result = (float(all_data['purchase_time'].count())/number)*100 #83.11%
#print(result)

"""
Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
How might Cool T-Shirts Inc. change their website to fix this problem?

The step with the highest dropout rate is the users who proceeded to checkout but did not purchase a t-shirt (83.11%).
Potential Solutions:

    1. Transparent Pricing: Ensure that all costs, including shipping fees and taxes, are clearly displayed before the checkout process. Unexpected costs can be a major turnoff.

    2. Streamlined Checkout Process: Simplify the checkout steps and minimize the number of clicks required to complete a purchase. A lengthy or complicated checkout process may deter users.

    3. Multiple Payment Options: Provide a variety of payment options to accommodate different user preferences. Lack of preferred payment methods can lead to abandonment.

    4. Trust Signals: Display trust badges, security certifications, and customer reviews to build confidence in the security and reliability of the website.

    5. Abandoned Cart Recovery: Implement strategies to remind users about items left in their carts, such as email reminders with incentives or discounts.
"""

#Let’s calculate the average time from initial visit to final purchase.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
#Calculate the average time to purchase
print(all_data.time_to_purchase.mean()) #0 days 00:43:53.360160

