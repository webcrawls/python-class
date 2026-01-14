# exercise_2_1_1.py


### General Notes

# Continuation characters
# "Block" - one or more statements inside, scoped, nested. whitespace deliminated
# Explicit / implicit statements, no lines over 80 char

### Lesson 2.1 Excercises
print("<2.1.1>")

first_name = "Kaden"
last_name = "Swallow"
course_code = "PROG12583"
number_of_courses = 5 # Until I book my elective
expected_grade = 110 # I will accept bonus marks


# Print all variables with one call to print, using f-strings for variable substitution
print(f"""---
Name: {last_name}, {first_name}
Taking {number_of_courses} courses through Sheridan College
Course Info: ({course_code}) (Expected grade: {expected_grade})
---""")

print("</2.1.1>")

### 2.1.2
print("<2.1.2>")

HARMONIZED_SALES_TAX_RATE = 0.13 # Remember, multiplying by this will return JUST the tax - not the full amount!
MONTHS_PER_YEAR = 12
CENTS_PER_QUARTER = 25
GRAVITATIONAL_CONSTANT = 9.8
SPEED_OF_LIGHT = 299_792_458 # m/s

print("Named constants defined")

print("</2.1.2>")

### 2.1.3

print("<2.1.3>")
to_scientific = [34_982.58, 0.004785, .1234567, 5]
from_scientific = [9.7824e3, 2.222e7, 1.987e-2, 5.5e-4]

for x in to_scientific:
    print(f"{x} -> {x:E}")

print('...')

for x in from_scientific:
    print(f"{x} -> {x:f}")

print("</2.1.3>")
### 2.1.4

print("<2.1.4>")

for x in to_scientific + from_scientific:
    print(f"{x} -> {x:.2e}")

print("</2.1.4>")

### 2.1.5
print("<2.1.5>")

int_num = 15
float_num = 23.5
str_num = '12.5'

print(f"int_num: {int_num}, as a float: {float(int_num)}, as a string: {str(int_num)}")
print(f"float_num: {float_num}, as int, as str")
str_num_parsed = float(str_num)
print(f"str_num: {str_num}, as int: {int(str_num_parsed)}, as float: {str_num_parsed} ")

print("</2.1.5>")