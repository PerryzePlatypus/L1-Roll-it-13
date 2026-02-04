want_instructions =input("Do you want to see the instructions?").lower()

if want_instructions == "yes" or want_instructions == "y":
    print("you said yes")
elif want_instructions == "no" or want_instructions == "n":
    print("you said no")
else:
    print("please enter yes/no")