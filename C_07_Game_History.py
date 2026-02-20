#Initialises list to hold game history

game_history = []

# get data (base component does this already, code below for testing purposes)
user_score = 0
comp_score = 0

while True:
    rounds_played= input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    comp_point = int(input("Computer points? "))
    winner = input("Who won? ")
    user_score = int(input("User Score: "))
    comp_score = int(input("Computer score: "))

    game_results = (f"Round {rounds_played}: User Points: {user_points} | "
                       f"Computer Points {comp_point}, {winner} wins "
                    f"({user_score} | {comp_score})")


    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)