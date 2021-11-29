# Mike Wilson 29 November 2021
# This program attempts to read the sales amounts in totals.txt and calculate
# total sales.

filename = 'cafe\\totals.txt'

# Variable for storing sales totals
total = 0

h = open(filename, 'r')

content = h.read()

for line in content:
  for i in line:
    if i.isnumeric() == True:
      # print(i)
     total += int(i)

print("Total sales so far: $", total)

# def calculate_total_sales():
  # '''Main function to calculate total sales from sales.txt'''