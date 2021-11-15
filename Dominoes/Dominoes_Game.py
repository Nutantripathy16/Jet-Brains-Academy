# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:25:02 2021

@author: NutanTripathy
"""
import random
dominoes_element = []    
Stock_pieces = []
Computer_pieces = []
Player_pieces = []
comp = []
play = []
domino = []


for i in range(7):
    for j in range(7):
        if (([i,j] not in dominoes_element) and ([j,i] not in dominoes_element)):
            dominoes_element.append([i,j])

while(True):      
    stock_pieces = random.sample(dominoes_element, 14)
    update1 = [item for item in dominoes_element if item not in Stock_pieces]
    Computer_pieces = random.sample(update1, 7)
    update2 = [item for item in dominoes_element if (item not in Stock_pieces and item not in Computer_pieces) ]
    Player_pieces = random.sample(update2, 7)
    for i in Computer_pieces:
        if i[0] == i[1]:
            comp.append(i) 
            
    for i in Player_pieces:
        if i[0] == i[1]:
            play.append(i) 
    if len(comp)!= 0 and len(play)!=0:
        max1 = max(comp)
        max2 = max(play)
        if max1 > max2:
            status = "player"
            domino.append(max1) 
            Computer_pieces.remove(max1)
            print("="*70)
            print("Stock pieces:",len(stock_pieces))  
            print("Computer pieces:",len(Computer_pieces),"\n")
            print("Domino snake:",domino,"\n")
            print("Your pieces:\n")
            count = 1
            for i in Player_pieces:
                print(f"{count}:{i}")
                count = count + 1
            print("\n")
            print("It's your turn to make a move. Enter your command.")
        elif max1 < max2:
            domino.append(max1)
            Player_pieces.remove(max2) 
            status = "computer"
            print("="*70)
            print("Stock pieces:",len(stock_pieces))  
            print("Computer pieces:",len(Computer_pieces),"\n")
            print("Domino snake:",domino,"\n")
            print("Your pieces:\n")
            count = 1
            for i in Player_pieces:
                print(f"{count}:{i}")
                count = count + 1
            print("\n")
            print("Status: Computer is about to make a move. Press Enter to continue...")
        
        break
    else:
        continue
        
        
    
    
    