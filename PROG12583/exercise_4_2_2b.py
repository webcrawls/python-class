# exercise 4.2.2b
# Ask the user to enter value from the keyboard.
# If the user enters a value that is made out of numbers only,
# display the square root of that number.
# Otherwise, display the letters that the user may have entered in uppercase.
# Get the input from the user
# If the input is made out of digits, calculate and display the square root
# Otherwise display the letters in uppercase.
import math

val = input("Provide a value:")

if val.isdigit(): # 
    print(math.sqrt(int(val)))
else:
    letters = [x for x in val if x.isalpha()]
    print(''.join(letters).upper())