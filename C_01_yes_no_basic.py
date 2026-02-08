
def yes_no(question):

    #Check users response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

            #checks if user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")


# Main routine


want_instructions = yes_no("Do you want to see the instructions? ").lower
want_coffee = yes_no("DO you want coffee?")

print("We done")