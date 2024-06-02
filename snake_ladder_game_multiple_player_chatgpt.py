import random

class IDice:
    def roll(self):
        raise NotImplementedError

class IGameRules:
    def apply_rules(self, position):
        raise NotImplementedError

class Dice(IDice):
    def roll(self):
        return random.randint(1, 6)

class SnakeLadderRules(IGameRules):
    def __init__(self, ladders, snakes):
        self.ladders = ladders
        self.snakes = snakes

    def apply_rules(self, position):
        if position in self.ladders:
            return self.ladders[position]
        if position in self.snakes:
            return self.snakes[position]
        return position

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1
        self.turns = 0

class Game:
    END_POINT = 30

    def __init__(self, players, dice, rules):
        self.players = players
        self.dice = dice
        self.rules = rules

    def start(self):
        turn_number = 0
        while len(self.players) > 1:
            turn_number += 1
            print(f"\nTurn {turn_number}")

            for player in list(self.players):
                choice = input(f"{player.name}, please roll the dice (Y to Roll, N to Withdraw): ").upper()

                if choice == "N":
                    print(f"{player.name} has withdrawn from the game.")
                    self.players.remove(player)
                    if len(self.players) == 1:
                        print(f"Congratulations {self.players[0].name}, you have won the game by default!")
                        return
                elif choice == "Y":
                    self.play_turn(player, turn_number)
                    if player.position == self.END_POINT:
                        print(f"Congratulations {player.name}, you have reached the end point and won the game!")
                        self.players.remove(player)
                    elif player.position > self.END_POINT:
                        player.position -= self.dice.roll()  # Move back to the original position
                        print(f"{player.name}, you need exactly {self.END_POINT - player.position} to win. Roll again.")
                else:
                    print("Invalid input. Please enter 'Y' to roll or 'N' to withdraw.")

        winner = self.determine_winner()
        print("\nGame Results:")
        print(winner)

    def play_turn(self, player, turn_number):
        player.turns = turn_number
        dice_number = self.dice.roll()
        print(f"{player.name}, you rolled a {dice_number}")
        player.position += dice_number
        player.position = self.rules.apply_rules(player.position)
        print(f"{player.name}, your position is now {player.position}")

    def determine_winner(self):
        min_turns = float('inf')
        winners = []

        for player in self.players:
            if player.turns < min_turns:
                min_turns = player.turns
                winners.clear()
                winners.append(player)
            elif player.turns == min_turns:
                winners.append(player)

        if len(winners) == 1:
            return f"The winner is: {winners[0].name}"
        else:
            return f"The joint winners are: {', '.join([p.name for p in winners])}"

def get_player_names(num_players):
    players = []
    for _ in range(num_players):
        name = input("Enter your name: ")
        players.append(Player(name))
    return players

if __name__ == "__main__":
    print("\nWelcome to Snake and Ladder game (Python Version)\n")
    num_players = int(input("How many players are going to play: "))

    players = get_player_names(num_players)
    dice = Dice()
    rules = SnakeLadderRules(
        {3: 22, 5: 8, 11: 26, 20: 29},
        {17: 4, 19: 7, 21: 9, 27: 1}
    )

    game = Game(players, dice, rules)
    game.start()
