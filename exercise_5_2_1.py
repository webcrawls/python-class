cont_input = 'y'

while cont_input.strip().lower() == 'y':
    values_input = input("Enter two numbers to be added:")
    first, second = values_input.split()

    value = float(first) + float(second)
    print(f"{first} + {second} = {value}")

    cont_input = input("Continue? (y/n)")
