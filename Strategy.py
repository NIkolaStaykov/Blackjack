#!/usr/bin/env python
# coding: utf-8


class Player():
    def __init__(self, bankroll):
        self.bankroll = bankroll 

    def choose_action(self, my_cards, dealer_card):
        values = []
        aces = my_cards.count('A')
        if aces == 1:
            hard = False
        else:
            hard = True
        for card in my_cards:
            values.append(self.determine_value(card))        
            
        dealer_card = self.determine_value(dealer_card)
        power = self.hand_to_value(my_cards)
        
        if(len(values) == 2 and values[0] == values[1]):
            if(values[0] in [11, 8]):
                return "split"
            if(values[0] == 9):
                if(dealer_card in [7, 10, 11]):
                    return "stand"
                else:
                    return "split"
            if(values[0] == 7):
                if(dealer_card <= 7):
                    return "split"
                else:
                    return "hit"
            if(values[0] == 6):
                if(dealer_card <= 6):
                    return "split"
                else:
                    return "hit"
            if(values[0] == 4):
                if(dealer_card in [5, 6]):
                    return "split"
                else:
                    return "hit"
            if(values[0] in [2, 3]):
                if(dealer_card <= 7):
                    return "split"
                else:
                    return "hit"
                
                
        if(hard == 1):
            
            if(power in range(4, 9)):
                return "hit"
            
            elif(power == 9):
                if(dealer_card == 2 or dealer_card >= 7):
                    return "hit"
                elif(dealer_card in range(3, 7)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                    
            elif(power == 10):
                if(dealer_card >= 10):
                    return "hit"
                elif(dealer_card in range(2, 10)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                    
            elif(power == 11):
                if(dealer_card == 11):
                    return "hit"
                elif(dealer_card in range(2, 11)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                    
            elif(power == 12):
                if(dealer_card in range(4, 7)):
                    return "stand"
                else:
                    return "hit"
            
            elif(power in range(13, 17)):
                if(dealer_card <= 6):
                    return "stand"
                else:
                    return "hit"
                
            elif(power >= 17):
                return "stand"
            
        elif(hard == 0): 
            
            if(power in range(13, 15)):
                if(dealer_card in range(5, 7)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                else:
                    return "hit"
                
            elif(power in range(15, 17)):
                if(dealer_card in range(4, 7)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                else:
                    return "hit"
                
            elif(power == 17):
                if(dealer_card in range(3, 7)):
                    if(len(my_cards) == 2):
                        return "double"
                    else:
                        return "hit"
                else:
                    return "hit"
                    
            elif(power == 18):
                if(dealer_card >= 9):
                    return "hit"
                elif(dealer_card in range(3, 7)):
                    if(len(my_cards) <= 2):
                        return "double"
                    else:
                        return "stand"
                else:
                    return "stand"

            elif(power >= 19):
                return "stand"




    def determine_value(self, card):    
        if(card in ["J", "Q", "K"]):
            value = 10
        elif(card == "A"):
            value = 11
        else:
            value = int(card)
        
        return value
    
    def hand_to_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card in self.deck.face_cards:
                value = value + 10
            elif card == 'A':
                value = value + 11
                aces = aces + 1
            else:
                value = value + int(card)
        while (value > 21 and aces > 0):
            value = value - 11
            aces = aces -1
        return value


# In[ ]:




