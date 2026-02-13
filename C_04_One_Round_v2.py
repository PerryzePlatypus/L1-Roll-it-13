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

#initialise rounds points


#roll the dice for the user and note if they got double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

#Retrieves user points
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

if double_user == "yes":
       print("GREAT NEWS - if you win, you will earn DOUBLE POINTS")

#assume user goes first
first = "user"
second = "computer"
player_1_points = user_points
player_2_points = comp_points

#if user has fewer points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

elif user_points == comp_points:
    print("The initial rolls were the same, the user starts!")
#if the computer has fewer points, switch the computer to player 1
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first
#loop until we have a winner
    
while player_1_points < 13 and player_2_points < 13:
    print()
    input("Press <enter> to continue this round\n")

#first person rolls the die and score is updated
    player_1_roll = random.randint( 1, 6)
    player_1_points += player_1_roll

    print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

    #if the first person score is over 13, ends round
    if player_1_points >= 13:
        break

# second person rolls the die and score is updated
    player_2_roll = random.randint(1, 6)
    player_2_points += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    print(f"{first}: {player_1_points} | {second} {player_2_points} ")
    
print("end of round")


