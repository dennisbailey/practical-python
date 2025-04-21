# mortgage.py

STARTING_PRINCIPAL = 500000.0
RATE = 0.05
MONTHLY_RATE = (1 + RATE / 12)
MONTHLY_PAYMENT = 2684.11

# Exercise 1.7: Dave’s mortgage
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation.
# The interest rate is 5% and the monthly payment is $2684.11.
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

print('Exercise 1.7: Dave’s mortgage')

principal = STARTING_PRINCIPAL
total_paid = 0.0
months = 0

while principal > 0:
    principal = principal * MONTHLY_RATE - MONTHLY_PAYMENT
    total_paid += MONTHLY_PAYMENT
    months += 1

print(f'Total paid: ${total_paid:,.2f}\n')
print('---------------------\n')

# Exercise 1.8: Extra payments
# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

print('Exercise 1.8: Extra payments\n')

monthly_extra_payment = 1000
number_of_extra_payment_months = 12

principal = STARTING_PRINCIPAL
total_paid = 0.0
months = 0

while principal > 0:
    extra = monthly_extra_payment if months < number_of_extra_payment_months else 0
    payment = MONTHLY_PAYMENT + extra

    principal = principal * MONTHLY_RATE - payment
    total_paid += payment
    months += 1

print(f'Total paid: ${total_paid:,.2f}')
print(f'Number of months: {months}\n')
print('---------------------\n')

# Exercise 1.9: Making an Extra Payment Calculator
# Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

print('Exercise 1.9: Making an Extra Payment Calculator\n')

extra_payment_start_month = 61
extra_payment_end_month = 108
monthly_extra_payment = 1000

principal = STARTING_PRINCIPAL
total_paid = 0.0
months = 0

while principal > 0:
    extra = monthly_extra_payment if extra_payment_start_month <= months + 1 <= extra_payment_end_month else 0
    payment = MONTHLY_PAYMENT + extra

    principal = principal * MONTHLY_RATE - payment
    total_paid += payment
    months += 1

print(f'Total paid: ${total_paid:,.2f}')
print(f'Number of months: {months}\n')
print('---------------------\n')


# Exercise 1.10: Making a table
# Modify the program to print out a table showing the month, total paid so far, and the remaining principal. The output should look something like this:
#
# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total paid 880074.1
# Months 310

print('Exercise 1.10: Making a table\n')

extra_payment_start_month = 61
extra_payment_end_month = 108
monthly_extra_payment = 1000

principal = STARTING_PRINCIPAL
total_paid = 0.0
months = 0

while principal > 0:
    extra = monthly_extra_payment if extra_payment_start_month <= months + 1 <= extra_payment_end_month else 0
    payment = MONTHLY_PAYMENT + extra

    principal = principal * MONTHLY_RATE - payment
    total_paid += payment

    # Print table
    print(f'{months + 1} ${total_paid:,.2f} ${principal:,.2f}')

    months += 1

print(f'Total paid: ${total_paid:,.2f}')
print(f'Number of months: {months}\n')
print('---------------------\n')

# Exercise 1.11: Bonus
# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.

print('Exercise 1.11: Bonus\n')

extra_payment_start_month = 61
extra_payment_end_month = 108
monthly_extra_payment = 1000

principal = STARTING_PRINCIPAL
total_paid = 0.0
months = 0

while principal > 0:
    extra = monthly_extra_payment if extra_payment_start_month <= months + 1 <= extra_payment_end_month else 0
    payment = MONTHLY_PAYMENT + extra

    # Correct for possible overpayment in the last month
    if principal * MONTHLY_RATE < payment:
        payment = principal * MONTHLY_RATE
        principal = 0
    else:
        principal = principal * MONTHLY_RATE - payment

    total_paid += payment

    # Print table
    # print(f'{months + 1} ${total_paid:,.2f} ${principal:,.2f}')

    months += 1

print(f'Total paid: ${total_paid:,.2f}')
print(f'Number of months: {months}\n')
print('---------------------\n')