#   RECURSIVE SIGMA Write a recursive function that given a number returns the sum of integers from 1 to that number.
def sigma(x):
    if x<=1:
        return x
    else:
        return x + sigma(x-1)

print(sigma(3))

#   RECURSIVE FACTORIAL Write a recursive function that given a number returns the sum of integers from 1 to that number.
def factorial(x):
    if x <=0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))