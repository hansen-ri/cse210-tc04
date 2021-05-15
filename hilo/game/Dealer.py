import random




class Dealer:




    def next_card():
        from game.Player import Player
        correntNumber = random.randint(1, 13)
        #print(f"The correct card number {correntNumber}")
        Player.guess_hl(correntNumber)

    def display_card():
        pass
    def game_over():
        pass
        print("The game is over")