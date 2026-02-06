# KadenSwallowLab4.py
# Author: Kaden Swallow
# Date: 2/6/26 (j cole just dropped)
    
# Description: A program which calculates a salary which increases
# each day, and formats the results as a nicely spaced table for the user.


# I noticed that the earning goes up by powers of two, starting at 2^0.
# Therefore, we can define a function which finds the power of 2
# and divide it by 100, to get our 'salary in cents'.
# 
# I previously made the 2 a constant as well, but it doesn't really make
# sense to, imo, as I think it is more of an implementation detail.
# 
# PS: I know we haven't learned lambdas yet (will we?), but they are
# cool, so... uhh.. yes! (Maybe i overcomplicated this but its cleannn)
SALARY_FUNCTION = lambda x: (2 ** x) / 100

# State - set balance and current_salary to zero.
balance = 0
days = int(input("Enter the number of days: "))

# Print our titles
print(f"{'Day' :4} {'Earning' :9} {'Total' :6}")
print('-' * 21)

# Iterate over each day, starting at zero and ending at DAYS - 1 (9).
for i in range(0, days):
    # Calculate the current salary for today, then add it to balance
    current_salary = SALARY_FUNCTION(i)
    balance += current_salary

    # (PS 2: I am sorta struggling to grasp string formatting, but I think
    # this is pretty close to what we were shown.)
    print('{:2}    {}     {:5}'.format(i+1, current_salary, round(balance, 2)))
