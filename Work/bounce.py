# bounce.py
#
# Exercise 1.5

# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell.
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.
# Round the output to 4 digits.
#
# 1 60.0
# 2 36.0

starting_height = 100
bounce_percentage = 0.6

for i in range(1,11):
    bounce_height = starting_height * (bounce_percentage)**(i+1)
    print(i, round(bounce_height, 4))
