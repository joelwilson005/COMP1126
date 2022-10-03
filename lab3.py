# COMP1126 Lab 3
# Joel Wilson 620098136
# October 3, 2022

# -----------------------------------------------------------------------------------------------
# Question 1
# -----------------------------------------------------------------------------------------------
def cubicSeries(n):
    """Function which takes an integer n and add the
    sequence of numbers which are cubed from the beginning to the integer. If n is less than or
    equal to 0 then the function must return 0. """

    # Check to see if n==0 and return 0 if n does == 0
    if n <= 0:
        return 0
    else:
        # Declare variable which stores the sum of cubed integers.
        cubeSeriesSum = 0

        # Counter variable used in while loop.
        i = 1

        while i < n + 1:
            # Add cubed value of counter variable to overall sum
            cubeSeriesSum = cubeSeriesSum + i ** 3

            # Increment the counter variable.
            i = i + 1

    return cubeSeriesSum

# -----------------------------------------------------------------------------------------------
# Question 2
# -----------------------------------------------------------------------------------------------
def cubicSeries_r(n):
    """Function which takes an integer n and add the
    sequence of numbers which are cubed from the beginning to the integer. If n is less than or
    equal to 0 then the function must return 0. The cube of the input n MUST be inclusive."""

    # This check is done to ensure that infinite recursion does not occur.
    if n <= 0:
        return 0
    else:
        # Add value of of n cubed to the sum and this function being called with argument of n-1
        cubicSum = n ** 3 + cubicSeries_r(n - 1)
        return cubicSum

# -----------------------------------------------------------------------------------------------
# Question 3
# -----------------------------------------------------------------------------------------------
def power(n):
    """Function that raises an integer n to its nth power and returns that
    value. If n is less than or equal to 0 then the function should return 0."""

    if n <= 0:
        return 0
    else:
        return n ** n

# -----------------------------------------------------------------------------------------------
# Question 4
# -----------------------------------------------------------------------------------------------
def sumSeries(n):
    """Function that returns the sum of  1^n + 2^n + ...n^n"""

    # Check to prevent infinte recursion.
    if n <= 0:
        return 0
    else:
        total = power(n) + sumSeries(n - 1)
        return total