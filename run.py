
def get_numbers_input():
    print("Please choose what arithmetic operation you wish to perform")
    print("You can enter the following options: h, x, +, -, *, /")

    while True:
        option = input("Please enter an option:\n")

        if validate_option(option):
            print("valid option!")
            break
    return option


def validate_option(option):
    """
    raises valueError if a value other than
    the ones mentioned in the print statement is entered
    """
    # print(values)
    try:
        options = ['h', 'x', '+', '-', '*', '/']
        if option not in options:
            raise ValueError(
                f"Wrong option entered! You can enter only h, x, +, -, *, /"
            )
    except ValueError as e:
        print(f"Invalid option: {e}, please try again.\n")
        return False

    return True

option = get_numbers_input()