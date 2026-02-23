import random


def initial_points(which_player):
    """Roll the dice twice and return total / if double points apply!"""

    double = "no"
    # Roll teh dice for the user ad note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two

    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double

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


def int_check():
#checks if users integer is equal or more than 13
    error = "Please enter an integer more than 0"

    while True:
        try:
            response = int(input("What is the Game Goal?"))

            if response < 0 :
                    print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ***

Roll the dices and try to win!
    """)

def make_statement(statement, decoration):
    """ADDS EMOJI / ADDITIONAL CHARACTER TO THE START AND ENDING OF HEADINGS"""
    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")



#At the start of the game, the computer / user score are both at ZERO
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

make_statement("Welcome to the Roll It 13 Game!", "🍀🎲")


# ask the user if they want instructions (check if yes / no)
want_instructions = yes_no("Do you want to see the instructions? ( Yes / No )")

# Displays the instruction if the user wants to see them
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()

print(game_goal)

#Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:
    rounds_played += 1


    #STart of round loop
    make_statement(f"Round {rounds_played}", "🎲")

    # ROll the dice for the user and note if they got a double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Retrieves user points
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # lets the user know if they qualify for double points
    if double_user == "yes":
        print("GREAT NEWS - if you win, you will earn DOUBLE POINTS")

    # assume user goes first
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the Computer\n")

    elif user_points == comp_points:
        print("The initial rolls were the same, the User starts!")
    # if the computer has fewer points, switch the computer to player 1
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first
    # loop until we have a winner

    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # first person rolls the die and score is updated

        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person score is over 13, ends round
        if player_1_points >= 13:
            break

        # second person rolls the die and score is updated
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second}: {player_2_points}")


    # associates player points with either the user or computer

    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first

    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # works out who won

    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset to zero"

    # doubles user points if eligible

    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output round results
    make_statement("Round Results!", "*")
    print(f"User Points: {user_points} | Computer Points: {comp_points}")
    print(round_feedback)
    print()

    #OUtside rounds loop - Update score with round points, only add point to the score of the
    comp_score += comp_points
    user_score += user_points

# Generates round results and add it to the game history list
    game_results = (f"Round {rounds_played}: User Points: {user_points} | "
                    f"Computer Points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

    # Shows overall scores (add this to rounds loops)
    print("     *** GAME UPDATE ***") #replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score {comp_score}")

    #ends the entire game, outputs final results
make_statement("GAME OVER", "🏁")

print()
if user_score > comp_score:
    make_statement("The USER won!", "👤")
else:
    make_statement("The COMPUTER won!", "💻")

print()
make_statement("Game History", "📃")

for item in game_history:
    print(item)