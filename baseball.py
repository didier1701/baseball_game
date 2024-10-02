import random

# A list to store all teams.
Teams = []

# Class to represent a team with attributes: name, attack, and defence.
class Team:
    def __init__(self, name, attack, defence):
        # Initialize the team's name, attack, and defence attributes.
        self.name = name
        self.attack = attack
        self.defence = defence

    # Method to display information about the team.
    def info(self):
        # Prints the team's name, offensive, and defensive power.
        print(f'{self.name} : offensive power: {self.attack} / defensive power: {self.defence}')


def create_teams():
    global Teams  # Access the global list of Teams.
    # Create three teams with different attack and defence values.
    team1 = Team('Attackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    # Store the teams in the `Teams` list.
    Teams = [team1, team2, team3]


def show_teams():
    # Initialize a counter to display team numbers.
    team_number = 1
    print('Information of all teams:')
    # Loop through each team in the `Teams` list.
    for team in Teams:
      
        print(str(team_number))
        # Call the `info()` method to display the team's details.
        team.info()
       
        team_number += 1


def play():
    print('Debug: play()')  
    create_teams()  
    show_teams()    .


play()
