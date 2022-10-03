# COMP1126 Lab Number 1
# Joel Wilson 620098136
# September 19, 20222

def mystery():
    """Python program that takes user's cell phone number's last digit
     and birth year and returns a 3-digit number where
     the first digit is the phone number's last digit and the last
     2 digits is the user's age (this year)."""

    #Obtain last digit of user's cell phone number and convert it into an integer.
    last_digit = int(input("Please enter the last digit of your cell phone number: "))


    # Obtain user's birth year in the format 'YYYY' and convert it into an integer.
    birth_year = int(input("Please enter your birth year in the format YYYY: "))

    #Return mystery number.
    return ((last_digit * 2 + 5) * 50 + 1772) - birth_year


def fuzzbiz(number):
    """Program which takes a number as input. If the number is
        divisible by 3 return the string “Fuzz”, if the number is
        divisible by 5 return the string “Biz”
        and if the number is divisible by both numbers then return
        the string “FuzzBiz”. If it is only
        any of the above cases then the program should return “No Fuzz No Biz” """

    if number % 3 == 0 and number % 5 == 0: return "FuzzBiz"

    elif number % 3 == 0: return "Fuzz"

    elif number % 5 == 0: return "Biz"

    else: return "No Fuzz No Bizz"
  

def is_leap_year(year):
    """Function that tests to see if a given year is a leap year or not."""

    #Check to see if year is a non-centurial leap year.
    if (year % 4 == 0) and (year % 100 > 0):
        return True

    #Check to see if year is a centurial leap year.
    elif (year % 100 == 0) and (year % 400 == 0):
        return True

    #Return False when year is not a leap year.
    else: return False