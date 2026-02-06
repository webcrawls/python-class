# Banks usually apply what is called "compound interest rates" on investments, which means 
# that the interest rate is applied not only to the principal amount, but also to the 
# interest earned during the previous maturity period. Usually the maturity period is one year.
#
# Write a program that will prompt the user to enter an investment amount and the interest 
# rate and calculates and displays the balance at the end of each year for 5 years. 
# The following is the program interaction where the prompt is in blue and user input in red:
#
# Enter investment amount: 1000
# Enter interest rate: 10
# After year 1  $1,100.00
# After year 2  $1,210.00
# After year 3  $1,331.00
# After year 4  $1,464.10
# After year 5  $1,610.51

investment = float(input("Enter investment amount:"))
interest_rate = float(input("Enter interest rate (0.0-1.0, or 0 to 100):"))

if interest_rate > 1:
    interest_rate = interest_rate / 100

YEARS = 5

account_value = investment

for year in range(1, YEARS + 1):
    account_value = account_value * (1 + interest_rate)
    print(f"After year {year}: ${account_value:.2f}")