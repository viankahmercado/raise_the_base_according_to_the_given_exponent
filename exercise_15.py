# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 15: 
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# use function with loop
def raise_exponent(base, exponent):
    result = 1

    for i in range(exponent):
        result *= base

    return result

# assign variables
base_value = 6
exponent_value = 3
result = raise_exponent(base_value, exponent_value)

# print to check