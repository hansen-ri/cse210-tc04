#import dealer
import random


class Player:


    def guess_hl( correntNumber):
        from game.Score import Score

        newNumber = random.randint(1, 13)
        print(f"The card is: {correntNumber}")
        hl = input(f"Higher or Lower? [h/l] ")
        print(f"Next card was: {newNumber}")
        if hl.lower() == "h":
            if correntNumber < newNumber:
                Score.calculate_score(100)
            else:
                Score.calculate_score(-75)

        elif hl.lower() == "l":
            if correntNumber > newNumber:
                Score.calculate_score(100)
            else:
                Score.calculate_score(-75)
        else:
            print("Please enter h/l again")
            print()
            print("...")
            print()
            Player.guess_hl(correntNumber)

    def play_again():
        from game.Score import Score
        from game.Dealer import Dealer
        playAgain = input("Keep playing? y/n ")
        if playAgain.lower() == "y":
            print()
            print("...")
            print()
            Dealer.next_card()
        else:
            Dealer.game_over()




            
