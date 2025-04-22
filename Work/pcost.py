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


# Exercise 1.30: Turning a script into a function

def portfolio_cost(filename):
    """
    Calculate the total cost of a stock portfolio.
    :param filename: The name of the CSV file containing the portfolio data.
    :return: The total cost of the portfolio.
    """
    total_cost = 0.0

    file = open(filename, 'rt')
    next(file) # Skip the header line

    for line in file:
        row = line.split(',')

        total_cost += int(row[1]) * float(row[2])

    file.close()

    return total_cost

total_cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: ${total_cost:,.2f}')

# Exercise 1.31: Error handling

def portfolio_cost_with_validation(filename):
    """
    Calculate the total cost of a stock portfolio.
    :param filename: The name of the CSV file containing the portfolio data.
    :return: The total cost of the portfolio.
    """
    total_cost = 0.0

    file = open(filename, 'rt')
    next(file) # Skip the header line

    for i, line in enumerate(file, start=2):
        row = line.split(',')

        # Check if the row has exactly 3 columns
        if len(row) != 3:
            print(f"Line {i}: Invalid row - expected 3 columns, got {len(row)}")

        # Check if shares and price are valid numbers
        try:
            shares = int(row[1])
            price = float(row[2])

            if shares < 0 or price < 0:
                print(f"Line {i}: Negative values not allowed: shares={shares}, price={price}")
                continue

            total_cost += shares * price

        except ValueError as e:
            print(f"Line {i}: Invalid number format - {e}")
            continue

    file.close()

    return total_cost

total_cost = portfolio_cost_with_validation('Data/missing.csv')
print(f'Total cost: ${total_cost:,.2f}')

# Exercise 1.32: Using a library function

import csv

def portfolio_cost_with_library(filename):
    """
    Calculate the total cost of a stock portfolio.
    :param filename: The name of the CSV file containing the portfolio data.
    :return: The total cost of the portfolio.
    """
    total_cost = 0.0

    file = open(filename)
    rows = csv.reader(file)
    next(rows) # Skip the header line

    for i, row in enumerate(rows, start=2):
        # Check if the row has exactly 3 columns
        if len(row) != 3:
            print(f"Line {i}: Invalid row - expected 3 columns, got {len(row)}")

        # Check if shares and price are valid numbers
        try:
            shares = int(row[1])
            price = float(row[2])

            if shares < 0 or price < 0:
                print(f"Line {i}: Negative values not allowed: shares={shares}, price={price}")
                continue

            total_cost += shares * price

        except ValueError as e:
            print(f"Line {i}: Invalid number format - {e}")
            continue

    file.close()

    return total_cost

total_cost = portfolio_cost_with_library('Data/portfolio.csv')
print(f'Total cost: ${total_cost:,.2f}')


# Exercise 1.33: Reading from the command line

import csv
import sys

def portfolio_cost_for_cli(filename):
    """
    Calculate the total cost of a stock portfolio.
    :param filename: The name of the CSV file containing the portfolio data.
    :return: The total cost of the portfolio.
    """
    total_cost = 0.0

    file = open(filename)
    rows = csv.reader(file)
    next(rows) # Skip the header line

    for i, row in enumerate(rows, start=2):
        # Check if the row has exactly 3 columns
        if len(row) != 3:
            print(f"Line {i}: Invalid row - expected 3 columns, got {len(row)}")

        # Check if shares and price are valid numbers
        try:
            shares = int(row[1])
            price = float(row[2])

            if shares < 0 or price < 0:
                print(f"Line {i}: Negative values not allowed: shares={shares}, price={price}")
                continue

            total_cost += shares * price

        except ValueError as e:
            print(f"Line {i}: Invalid number format - {e}")
            continue

        total_cost += shares * price

    file.close()

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

total_cost = portfolio_cost_for_cli(filename)
print(f'Total cost: ${total_cost:,.2f}')