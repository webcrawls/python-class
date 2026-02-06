while True:
    values_input = input("Enter two numbers to be added:")
    values = values_input.split(" ")

    value = float(values[0]) + float(values[1])
    print(value)


    continue_input = input("Continue? (y/n)")
    if continue_input == 'n':
        exit() # or break