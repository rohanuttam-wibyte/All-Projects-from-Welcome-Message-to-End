import random 

# Requirement: At least one usage of a dictionary
striker = {
    "stamina": 100,
    "goals": 0,
    "funds": 50,
    "tournament_wins": 0
}

# Shop dictionary for training upgrades
training_academy = {
    "energy_drink": 15,
    "coaching_session": 30
}

# Requirement: Function with default arguments
def show_match_stats(player_data, show_welcome=False):
    if show_welcome:
        print("\n WELCOME TO STRIKER'S GLORY! ")
    print(f"\n Stamina: {player_data['stamina']}% | Goals: {player_data['goals']} | Funds: ${player_data['funds']}")
    print(f" Tournaments Won: {player_data['tournament_wins']}")
    print("-" * 45)

# Requirement: Function created with *args
def claim_sponsorship_deal(*rewards):
    print("\n BONUS: A local brand offered you a sponsorship deal!")
    for reward in rewards:
        if reward == "funds":
            striker["funds"] += 25
            print(" Gained $25 sponsorship bonus!")
        elif reward == "energy_drink":
            striker["stamina"] = min(100, striker["stamina"] + 20)
            print(" Drank a free sponsor energy drink! (+20% Stamina)")

show_match_stats(striker, show_welcome=True)

while striker["stamina"] > 0:
    print("\nWhat is your next move?")
    print("1. Take a Penalty Shot (Uses 20% Stamina)")
    print("2. Buy Energy Drink ($15 | Restores 40% Stamina)")
    print("3. Retire from the Tournament")
    
    # Requirement: User input handled with try/except
    try:
        choice = int(input("Action (1-3): "))
        
        if choice == 1:
            striker["stamina"] -= 20
            
            # Soccer Mechanic: Choose where to shoot
            print("\nWhere do you aim your shot?")
            print("1. Top Left | 2. Top Right | 3. Bottom Center")
            shot_direction = int(input("Aim (1-3): "))
            
            if shot_direction not in [1, 2, 3]:
                print("\n You kicked it completely wide out of bounds!")
                continue
                
            # Goalkeeper AI random dive choice
            gk_dive = random.randint(1, 3)
            
            if shot_direction == gk_dive:
                print("\n SAVED! The goalkeeper anticipated your shot.")
            else:
                striker["goals"] += 1
                striker["funds"] += 20
                print("\n GOAL!!! You successfully found the back of the net! (Earned $20)")
                
                # Check for an unexpected sponsorship trigger
                if random.random() < 0.35:
                    claim_sponsorship_deal("funds", "energy_drink")
                    
            # Check if you reached enough goals to win a trophy
            if striker["goals"] > 0 and striker["goals"] % 3 == 0:
                striker["tournament_wins"] += 1
                print("\n CHAMPION! You won the tournament bracket!")
                
        elif choice == 2:
            if striker["funds"] >= training_academy["energy_drink"]:
                striker["funds"] -= training_academy["energy_drink"]
                striker["stamina"] = min(100, striker["stamina"] + 40)
                print("\n Gulp! Energy drink consumed. Stamina restored.")
            else:
                print("\n Insufficient funds to purchase an energy drink!")
                
        elif choice == 3:
            print(f"\n You retired your player! Total career goals: {striker['goals']}")
            break
        else:
            print("\n Invalid match choice. Please pick 1, 2, or 3.")
            
    except ValueError:
        print("\n Referee Foul! Enter numbers only for your choices.")

    # Prints updated stats after every single turn finishes
    if striker["stamina"] > 0 and choice != 3:
        show_match_stats(striker)

if striker["stamina"] <= 0:
    print("\n Exhaustion! Your player collapsed from fatigue. Game Over.")