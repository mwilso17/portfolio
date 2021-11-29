# Mike Wilson 29 November 2021
# This program attempts to read the sales amounts in sales.txt and calculate
# total sales.

filename = 'cafe\\totals.txt'

# Variable for storing sales totals
total = 0

h = open(filename, 'r')

content = h.readlines()

for line in content:
  for i in line:
    if i.isdigit() == True:
      print(i)
      # total += int(i)

print("Total sales so far: $", total)

# def calculate_total_sales():
  # '''Main function to calculate total sales from sales.txt'''