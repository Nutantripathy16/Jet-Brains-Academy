# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:00:24 2021

@author: NutanTripathy
"""

import random
win = {"rock":["fire", "scissors", "snake", "human", "tree", "wolf","sponge"], "fire": ["scissors","snake", "human", "tree", "wolf", "sponge", "paper"], "scissors" : ["snake", "human", "tree", "wolf", "sponge","paper", "air"], "snake" : ["human", "tree","wolf" , "sponge","paper", "air", "water"], "human" : ["tree", "wolf" , "sponge","paper", "air", "water", "dragon"], "tree" : ["wolf" , "sponge","paper", "air", "water", "dragon", "devil"], "wolf": ["sponge","paper", "air", "water", "dragon", "devil", "lightning"], "sponge" : ["paper", "air", "water", "dragon", "devil", "lightning", "gun"], "paper" : ["air", "water", "dragon", "devil", "lightning", "gun", "rock"], "air" : ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"], "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"], "dragon" : ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"], "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"], "lightning" : ["gun", "rock", "fire", "scissors", "snake", "human", "tree"], "gun" : ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"]}
name_i = input("Enter your name: ")
print("Hello,",name_i)
with open("rating.txt", "r") as f:
    name_list = {}
    for line in f:
        name, rating = line.split()
        name_list[name] = int(rating)
f.close()
    
if name_i not in name_list.keys():
    name_list[name_i] = 0
 
for k,v in name_list.items():
    if k == name_i:
        get_rating = v
    
    elif  name_i not in name_list.keys():
        name_list[name_i] = 0
        get_rating = 0



cases_default = ["rock","scissors","paper"]

action = input("Enter your action : - ")
while(True):

    if action == "!exit":
        print("Bye!")
        break
    elif action =="!rating":
        print(name_list[name_i])

    elif action == "" :
        print("Okay, let's start")

        while (action == "" ):
            player_choice = input("Enter your choice to play :- ")
            if player_choice == "!exit":
                    action = "!exit"
                    print("Bye!")
                    break
            elif player_choice =="!rating":
                print(name_list[name_i])
                
            elif player_choice not in cases_default:
                    print("Invalid input") 
                    
            elif player_choice in cases_default:
                computer_choice = random.choice(cases_default)
                if player_choice == computer_choice:
                    get_rating = get_rating + 50
                    name_list[name_i] = get_rating
                    print(f"There is a draw ({player_choice})")
                elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock"):
                    print(f"Sorry, but the computer chose {computer_choice}")
                else:
                    get_rating = get_rating + 100
                    name_list[name_i] = get_rating
                    print(f"Well done. The computer chose {computer_choice} and failed") 
            
    else:
        print("Okay, let's start")
        player_choice = input("Enter your choice from the list :- ")
        cases_new = action.split(",")
        while (player_choice != "!exit"):
            if player_choice =="!rating":
                    print(name_list[name_i])
    
            elif player_choice not in cases_new:
                print("Invalid input") 
                        
            elif player_choice in cases_new:
                computer_choice = random.choice(cases_new)
                
                if computer_choice in win[player_choice]:
                    get_rating = get_rating + 100
                    name_list[name_i] = get_rating
                    print(f"Well done. The computer chose {computer_choice} and failed") 
                elif computer_choice == player_choice:
                    get_rating = get_rating + 50
                    name_list[name_i] = get_rating
                    print(f"There is a draw ({player_choice})")
                elif computer_choice not in win[player_choice]:
                    get_rating = get_rating + 0
                    name_list[name_i] = get_rating
                    print(f"Sorry, but the computer chose {computer_choice}") 
            player_choice = input("Enter your choice from the list :- ")
            if player_choice == "!exit":
                action = "!exit"
                print("Bye!")
                break
    
    if action == "!exit":
        break