
class Score:





    score = 300


    def calculate_score( numberToAddToScore):
        Score.score += numberToAddToScore
        print(f"Your score is: {Score.score}")
        Score.score_is_zero()

    def start_score():
        from game.Dealer import Dealer
        Score.score = 300
        Dealer.next_card()

    def score_is_zero():
        from game.Dealer import Dealer
        from game.Player import Player
        if Score.score <= 0:
            Dealer.game_over()
        else:
            Player.play_again()
