# Mike Wilson 29 November 2021
# This program attempts to emulate how a cafe's software may work to calculate
# sales totals and record purchases. 

from cafe_inventory import inventory, basket, subtotal
from datetime import date

# Get today's date so we can record it to sales.txt after purchase
today = date.today()

# Tax rate can be adjusted by changing the value. 0.05 = 5% tax rate
tax_rate = 0.05

# a file to record items sold
filename = 'cafe\sales.txt'

def calculate_total():
  '''Accepts user input, calculates subtotal, adds tax, rounds total'''
  active = True
  while active:
    user_input = input('Enter your next item (q to stop, i for inventory): ')

    if user_input == 'q':
      active = False
    elif user_input == 'i':
      print(inventory)
      user_input
    elif user_input not in inventory:
      print('Please enter an item from the inventory list.')
    elif user_input in inventory:
      print(f'Adding your {user_input} to the cart.')
      basket.append(user_input)
  
  print('Your cart contains: ', basket)

  for items in basket:
    subtotal.append(inventory[items])
  pre_tax_total = sum(subtotal)

  amount_to_pay = '{:.2f}'.format(round(pre_tax_total + (pre_tax_total * tax_rate), 2))

  print(f"Your total is: $", amount_to_pay)

  # records purchases and total to sales.txt
  with open(filename, 'a') as f:
    f.write(f"\n{today}\t {basket}\t {amount_to_pay}")


# Executes code
calculate_total()