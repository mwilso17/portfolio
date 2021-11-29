# Mike Wilson 29 November 2021
# This is an attempt to calculate total sales from totals.txt

filename = 'cafe\\totals.txt'

total = 0

with open(filename) as file_object:
  for line in file_object:
    total += float(line)

print(f"Total sales so far: $", total)