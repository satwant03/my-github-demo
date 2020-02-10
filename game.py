from card import *
import os 

def game():
    os.system("clear")
    abc = Deck()
    abc.shuffle()
    player1 = Hand()
    player2 = Hand()
    abc.move_cards(player1, 5)
    abc.move_cards(player2, 5)

    print("\nPlayer 1:\n--------------")
    print(player1)
    print("\nPlayer 2: \n--------------")
    print(player2)
    print("\n--------------")
    p1_score = 0
    p2_score = 0
    while (len(player1.cards) >0):
        p1_card = player1.pop_card()
        p2_card = player2.pop_card()
        if p1_card.rank > p2_card.rank:
            p1_score += 1
        elif p1_card.rank < p2_card.rank:
            p2_score += 1
    # print(p1_score," & ",p2_score)
    if p1_score > p2_score:
        print("Player 1 Wins!")
    elif p1_score < p2_score:
        print("Player 2 Wins!")
    else:
        print("No one Wins!")

if __name__ == '__main__':
    game()