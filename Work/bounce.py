# bounce.py
#
# Exercise 1.5

height = 100.0
bounce_number =1

while bounce_number < 11:
    height = .6 * height
    print(bounce_number, round(height,4))
    bounce_number = bounce_number + 1
