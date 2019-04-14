#/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Anthony Pitts

import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank    

    def __str__(self):
        return self.rank + " of " + self.suit

    def value(self, total):
        face_cards = ['J','Q','K']
        if self.rank=='A':
            if total<=10:
                return 11
            else:
                return 1
        else:
            if self.rank in face_cards:
                return 10
            else:
                return int(self.rank)


def make_deck():
    suits = ['♠','♣','♦','♥']
    deck = []
    for item in suits:
        for i in range(2,10):
            deck.append(item+str(i))
    random.shuffle(deck)
    return deck


def main():
    deck = make_deck()
    suits_dict = {'♠':"spades",'♣':"clubs",'♦':"diamonds",'♥':"hearts"}
    print("Welcome to Virtual Black Jack!")
    decision = ""
    ind = 0
    player_total = 0
    dealer_total = 0
    while decision!="n":
        print("You drew " + deck[ind])
        player_total = player_total + Card(suits_dict[deck[ind][0]],deck[ind][1:]).value(player_total)
        print("your sum: " + str(player_total))
        ind=ind+1
        if player_total==21:
            print("You Win!")
            return
        if player_total>21:
            print("You Lose!")
            return
        decision = input("Do you want another card? (y/n) ")
            
    #Dealer's turn
    print("My turn.")
    while dealer_total<17:
        print("I drew: " + deck[ind])
        dealer_total = dealer_total + Card(suits_dict[deck[ind][0]],deck[ind][1:]).value(dealer_total)
        print("My sum: " + str(dealer_total))
        ind = ind + 1
        if dealer_total == 21:
            print("You lose!")
            return
        if dealer_total>21:
            print("You win!")
            return
    if dealer_total==player_total:
        print("The game is a push! - Tie!")
        return
    if dealer_total>player_total:
        print("You Lose!")
        return
    else:
        print("You win!")
        return
    

if __name__ == "__main__":
    main()
