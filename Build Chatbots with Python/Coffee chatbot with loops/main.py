from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = "y"
  drinks = []
  while order_drink == "y":
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      order_drink = order_input("Would you like to order another drink? \n[a] y \n[b] n \n>")
      if order_drink == "y" or "n" or "yes" or "sure" or "no":
        break      
 
    
  name = order_input('Can I get your name please? \n> ')
  print('Okay, so I have:')
  for drink in drinks:
    print('-', drink)   
  print('Thanks, {}! Your order will be ready shortly.'.format(name))
      

def get_drink_type():
  res = order_input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return order_brewed_coffee()
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

  
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')
  
def get_size():
  res = order_input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

def order_latte():
  res = order_input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

  if res == 'a':
    return 'ordinary latte with 2% milk'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()
  
# Define new functions here!
def order_brewed_coffee():
  while True:
    res = order_input("Would you like to try coffee brewed fromPuerto Rico mami? \n[a] Yes! \n[b] No bozo \n>")
    if res == "a":
      return "Puerto Rico coffee"
    elif res == "b":
      return "ordinary brewed coffee"
    print_message()

def order_mocha():
  while True:
    res = order_input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>")
    if res == "a":
      return "peppermint mocha"
    elif res == "b":
      return "mocha"
    print_message()

# Returns user input or returns to the beginning if the input is "stop" (order is cancelled).
def order_input(text):
    res = input(text)
    if res == "stop":
        print("Order cancelled!")
        coffee_bot()
    else:
        return res

coffee_bot()
