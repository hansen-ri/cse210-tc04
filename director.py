def dealer():
    import random
    dealer_card = random.randint(1, 13)
    if dealer_card == 1:
        print("The card is: Ace")
    elif dealer_card == 11:
        print("The card is: Jack")
    elif dealer_card == 12:
        print("The card is: Queen")
    elif dealer_card == 13:
        print("The card is: King")
    else
        print("The card is: " + dealer_card)
    next_card = random.randint(1, 13)
    guess_hl(next_card)
    