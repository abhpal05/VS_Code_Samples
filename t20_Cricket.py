import random

# Constants
OVERS = 20
BALLS_PER_OVER = 6

# Define players for two teams
team1_players = ["Player1_T1", "Player2_T1", "Player3_T1", "Player4_T1", "Player5_T1", 
                 "Player6_T1", "Player7_T1", "Player8_T1", "Player9_T1", "Player10_T1", "Player11_T1"]

team2_players = ["Player1_T2", "Player2_T2", "Player3_T2", "Player4_T2", "Player5_T2", 
                 "Player6_T2", "Player7_T2", "Player8_T2", "Player9_T2", "Player10_T2", "Player11_T2"]

# Simulate an over
def simulate_over():
    runs = 0
    wickets = 0
    for ball in range(BALLS_PER_OVER):
        outcome = random.choices(["0", "1", "2", "3", "4", "6", "W"], [30, 25, 10, 5, 15, 10, 5])[0]
        if outcome == "W":
            wickets += 1
        else:
            runs += int(outcome)
    return runs, wickets

# Simulate a single innings
def simulate_innings(team_players):
    total_runs = 0
    total_wickets = 0
    for over in range(OVERS):
        if total_wickets >= 10:  # All players are out
            break
        runs, wickets = simulate_over()
        total_runs += runs
        total_wickets += wickets
        print(f"Over {over+1}: Runs = {runs}, Wickets = {wickets}")
        print(f"Total Runs: {total_runs}/{total_wickets}")
    return total_runs, total_wickets

# Simulate the T20 match
def simulate_match():
    print("Team 1 Batting:")
    team1_score, team1_wickets = simulate_innings(team1_players)
    print(f"Team 1 Total Score: {team1_score}/{team1_wickets}\n")
    
    print("Team 2 Batting:")
    team2_score, team2_wickets = simulate_innings(team2_players)
    print(f"Team 2 Total Score: {team2_score}/{team2_wickets}\n")
    
    # Determine the winner
    if team1_score > team2_score:
        print("Team 1 wins!")
    elif team2_score > team1_score:
        print("Team 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    simulate_match()
