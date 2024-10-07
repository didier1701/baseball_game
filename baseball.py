import random
import math

# A list to store all teams.
Teams = []

# Global dictionary to store the selected teams for the player and the opponent.
playing_teams = {'myself': 'Your', 'enemy': "Opponent's"}

# Class to represent a team with attributes: name, attack, and defense.
class Team:
    def __init__(self, name, attack, defence):
        # Initialize the team with a name, attack power, and defense power.
        self.name = name
        self.attack = attack
        self.defence = defence
        self.total_score = 0  # Initialize total score to 0 for each team.

    # Method to display information about the team.
    def info(self):
        print(f'{self.name}: offensive power: {self.attack} / defensive power: {self.defence}')

    # Method to calculate hit rate based on offensive power (randomized between 10 and attack power).
    def get_hit_rate(self):
        return random.randint(10, self.attack)

    # Method to calculate out rate based on defensive power (randomized between 10 and defense power).
    def get_out_rate(self):
        return random.randint(10, self.defence)

# Function to create and add teams to the global list.
def create_teams():
    global Teams
    # Creating three teams with different offense and defense stats.
    team1 = Team('Attackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    
    # Add the teams to the global list.
    Teams.extend([team1, team2, team3])

# Function to display all available teams.
def show_teams():
    team_number = 1
    print('Information of all teams')
    
    # Loop through each team and display their info with numbering.
    for team in Teams:
        print(f'{team_number}')  # Display the team number.
        team.info()  # Call the info method to show team details.
        team_number += 1  # Increment team number.

# Function to allow team selection for either 'myself' or 'enemy'.
def choice_team(player):
    global playing_teams
    while True:
        try:
            # Ask the player to select a team (input is expected as an integer).
            selection = int(input(f"Select {playing_teams[player]} team (1-3) "))
            
            # If the input is valid (1, 2, or 3), select the team.
            if selection in [1, 2, 3]:
                selected_team = Teams[selection - 1]  # Select the team from the list (index starts at 0).
                playing_teams[player] = selected_team  # Assign selected team to the player.
                
                # Output which team has been selected.
                if player == 'myself':
                    print(f"Your team is '{selected_team.name}'")
                else:
                    print(f"Opponent’s team is '{selected_team.name}'")
                break  # Exit loop if selection is valid.
            else:
                print("Invalid input. Please select a team between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer inputs.

# Function to calculate the score for one inning with debug output.
def get_play_inning(inning):
    # Depending on the inning (top or bottom), get the hit and out rates.
    if inning == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inning == 'bottom':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()

    # Calculate score as the difference between hit rate and out rate divided by 10.
    score = (hit_rate - out_rate) / 10
    inning_score = math.floor(score)  # Use floor to get the integer part of the score.
    
    # If the score is negative, set it to 0.
    if inning_score < 0:
        inning_score = 0
    
    return inning_score  # Return the inning score.

# Main function to execute the game.
def play():
    create_teams()  # Create the teams.
    show_teams()  # Display the available teams.
    
    # Allow the player and the opponent to select their teams.
    choice_team('myself')
    choice_team('enemy')
    
    # Initialize the scoreboard with headers.
    score_boards = ['________|', 'You     |', 'Opponent|']
    
    # Simulate the game for 9 innings.
    for i in range(9):
        score_boards[0] += str(i+1) + '|'  # Add inning number to the scoreboard header.

        # Calculate and display the score for the top inning (player's turn).
        inning_score = get_play_inning('top')
        score_boards[1] += str(inning_score) + '|'  # Add score to player's row.
        playing_teams['myself'].total_score += inning_score  # Add to total score.
        
        # Special condition for the bottom of the 9th inning if the opponent is winning.
        if i == 8 and playing_teams['enemy'].total_score > playing_teams['myself'].total_score:
            score_boards[2] += 'X|1'  # Opponent wins, no need to play the 9th inning.
        
        # Calculate and display the score for the bottom inning (opponent's turn).
        inning_score = get_play_inning('bottom')
        score_boards[2] += str(inning_score) + '|'  # Add score to opponent's row.
        playing_teams['enemy'].total_score += inning_score  # Add to opponent's total score.
    
    # Add the total score ("R" for runs) to the scoreboard.
    score_boards[0] += 'R|'
    score_boards[1] += str(playing_teams['myself'].total_score) + '|'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '|'
    
    # Print the final scoreboard.
    print(score_boards[0])
    print(score_boards[1])
    print(score_boards[2])

# Start the game.
play()
