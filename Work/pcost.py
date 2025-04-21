# pcost.py
#
# Exercise 1.27: Reading a data file

# Now that you know how to read a file, let’s write a program to perform a simple calculation.

# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

# Hint: to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).

# Your program should print output such as the following:

# Total cost 44671.15

total_cost = 0.0

file = open('Data/portfolio.csv', 'rt')
headers = next(file) # Skip the header line

for line in file:
    row = line.split(',')

    total_cost += int(row[1]) * float(row[2])

file.close()

print(f'Total cost: ${total_cost:,.2f}')

# Exercise 1.28: Other kinds of “files”

import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')