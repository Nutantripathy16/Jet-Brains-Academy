# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:45:28 2021

@author: NutanTripathy
"""

class CoffeeMachine:
    
    
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        #initial state of machine taken in action
        self.state = 'action'
        self.exit = False
        self.action(self.state)
    
    def action(self, state):
        if state == "action": 
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy": 
                self.buy(self.water, self.milk, self.beans, self.cups, self.money)
            
            elif action == "fill":
                self.fill(self.water, self.milk, self.beans, self.cups, self.money)
              
            elif action == "take":
               self.take(self.water, self.milk, self.beans, self.cups, self.money)
            
            elif action == "remaining":
               self.remaining(self.water, self.milk, self.beans, self.cups, self.money)
                
            elif action == "exit":
                self.exit = True
        
        #if we want to exit then state change to exit and program will stop
        if self.exit:
               self.state = 'exit'

    def buy(self,water, milk, beans, cups, money): 
        to_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if to_buy == "1":
                self.buy_1(water, milk, beans, cups, money)
        elif to_buy == "2":
            self.buy_2(water, milk, beans, cups, money)
        elif to_buy == "3":
            self.buy_3(water, milk, beans, cups, money)
        else: 
            pass
        self.action(self.state)
        
    def buy_1(self,water, milk, beans, cups, money):
        if (water > 250 and beans > 16):
            print("I have enough resources, making you a coffee!")
            self.water = water - 250
            self.milk = milk - 0
            self.beans = beans - 16
            self.money = money + 4
            self.cups = cups - 1
        elif water < 250:
            print("Sorry, not enough water!")
        elif beans < 16:
            print("Sorry, not enough beans!")
        elif cups< 1:
            print("Sorry, not enough cups!")
        self.action(self.state)

    def buy_2(self, water, milk, beans, cups, money):
        if (water > 350 and milk > 75 and beans > 20):
            print("I have enough resources, making you a coffee!")
            self.water = water - 350
            self.milk = milk - 75
            self.beans = beans - 20
            self.money = money + 7
            self.cups = cups - 1
        elif water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif beans < 20:
            print("Sorry, not enough beans!")
        elif cups< 1:
            print("Sorry, not enough cups!")
        self.action(self.state)
       
                
    def buy_3(self, water, milk, beans, cups, money):
        if (water > 200 and milk > 100 and beans > 12):
            print("I have enough resources, making you a coffee!")
            self.water = water - 200
            self.milk = milk - 100
            self.beans = beans - 12
            self.money = money + 6
            self.cups = cups - 1
        elif water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif beans < 12:
            print("Sorry, not enough beans!")
        elif cups< 1:
            print("Sorry, not enough cups!")
        self.action(self.state)

            
    def take(self, water, milk, beans, cups, money):
        print(f"I gave you ${self.money}")
        self.money = self.money - money
        self.action(self.state)
        
    
    def fill(self, water, milk, beans, cups, money):
        water_f = int(input("Write how many ml of water you want to add:\n"))
        milk_f = int(input("Write how many ml of milk you want to add:\n"))
        beans_f = int(input("Write how many grams of coffee beans you want to add:\n"))
        cups_f = int(input("Write how many disposable coffee cups you want to add:\n"))
        self.water = water + water_f
        self.milk = milk + milk_f
        self.beans = beans + beans_f
        self.cups = cups + cups_f
        self.money = money + 0
        self.action(self.state)
        
    
    def remaining (self,water, milk, beans, cups, money):
        print(f"The coffee machine has:\n{water} of water\n{milk} of milk\n{beans} of coffee beans\n{cups} of disposable cups\n{money} of money")
        self.action(self.state)


        
    

coffee = CoffeeMachine( 400, 540, 120, 9, 550)
