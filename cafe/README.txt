This program models software that a cafe/kiosk may use to track 
the prices of its inventory, individual sale totals and date sold,
and total sales to date. The program writes to 2 seperate .txt files when ran.

cafe.py is the main program and is should be ran in a terminal. Users will enter
any items they wish to purchase from cafe_inventory.py and the program will calculate
sales total (sale + tax) for the user. cafe.py will also save these totals in 2 
seperate files (sales.txt which stores date of sale, items sold, and total, respectively
and totals.txt stores totals to be used by total_sales.py).

cafe_inventory.py stores the data associated with inventory.

total_sales.py calculates total sales to date when ran.