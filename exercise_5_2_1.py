while True:
    values_input = input("Enter two numbers to be added:")
    first, second = values_input.split()

    value = float(first) + float(second)
    print(f"{first} + {second} = {value}")


    continue_input = input("Continue? (y/n)")
    if continue_input.strip().lower() == 'n':
        exit() # or break