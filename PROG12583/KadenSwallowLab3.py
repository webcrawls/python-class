# Lab3.py
# Author: Kaden Swallow
# Date: January 30, 2026
  
# Description: A program that calculates the amount of interest gained on a
# given balance, and the number of years the money has been sitting there.

# Defining our interest values.
# All provided by our prof, and we use capitals to denote constants.
BASE_INTEREST = 0.025
EXTENDED_INTEREST = 0.055
TARGET_YEARS = 5

# Grab our inputs from the user - we need the account balance and the
# number of years to do our interest calculation.
balance_input = input("Enter your account balance: ")
years_input = input("Enter the number of years: ")


# Convert balance to float
balance = float(balance_input)

# Convert years to an int - presumably, would only ever be provided as
# an integer, but I dunno. I could be wrong, I'm not an accountant
years = int(years_input)

# Remembering interest = principal x annual rate x time (in years)
# Define our initial interest variable, starting at zero.
interest = 0

# if/else statement to determine if we should use the base or extended interest.
if years <= TARGET_YEARS:
    # If it is less than or equal to 5 (how I interpreted the question),
    # use BASE_INTEREST.
    interest += balance * BASE_INTEREST * years
else:
    # Likewise, if it's more than 5 years, use EXTENDED_INTEREST.
    interest += balance * EXTENDED_INTEREST * years

# Print out using f-strings, and the left-right align shorthand syntax.
# We could have also used ljust and rjust directly, but that costs more lines.
print(f"{'Old balance:':<20}{balance:>10.2f}")
print(f"{'Interest:':<20}{interest:>10.2f}")
print(f"{'New balance:':<20}{balance+interest:>10.2f}")