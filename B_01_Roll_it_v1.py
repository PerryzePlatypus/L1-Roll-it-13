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

def int_check():
#checks if users integer is equal or more than 13
    error = "Please enter an integer more than / equal to 13"

    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                    print(error)
            else:
                return response

        except ValueError:
            print(error)



# displays the instructions if the user wants
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)