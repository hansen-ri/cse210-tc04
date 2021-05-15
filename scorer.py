# TODO: Add entry point code here

#I was assigned the player class. 

#I need a guess_hl function.
def guess_hl():
    guess = input('Higher or lower? [h/l] ')

    display_card(card)

    while guess == 'h':
        if guess > card:
            print('Correct.')
            #Display and calculate score.
        elif guess < card: 
            print('Incorrect.')
            #Display and calculate score.
        else guess == card:
            print('Equal')
            #Display card.

    while guess == 'l':
        if guess > card:
            print('Incorrect.')
            #Display and calculate score.
        elif guess < card: 
            print('Correct.')
            #Display and calculate score.
        else guess == card:
            print('Equal.')
            #Display and calcualte score. 

#Call my function?
guess_hl()

#I need a play_again function.
def play_again():
    play = input('Keep playing? [y/n] ')

    if play == 'y':
        guess_hl()
    elif play == 'n':
        print('Good game. Bye.')
    else: 
        print('Invalid response. Game over. Bye.')

#Call my function?
play_again()

#Samantha Webb
#web18016@byui.edu