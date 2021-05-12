import random
dealer_card = random.randint(1, 13)
def check_card():
    if dealer_card == 1:
        print("The card is: Ace")
    elif dealer_card == 11:
        print("The card is: Jack")
    elif dealer_card == 12:
        print("The card is: Queen")
    elif dealer_card == 13:
        print("The card is: King")
    else:
        print(f"The card is: {dealer_card}")
check_card()
next_card = random.randint(1, 13)