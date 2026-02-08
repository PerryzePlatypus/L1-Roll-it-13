def yes_no(question):
    # Check users response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

        # checks if user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")


# Main routine

# Ask users if they want instructions (check if they say yes/no)
want_instructions = yes_no("Do you want to see the instructions? ")


def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ***

    Roll the dices and try to win!
    """)


# displays the instructions if the user wants
if want_instructions == "yes":
    instructions()

print()
print("Program continues")