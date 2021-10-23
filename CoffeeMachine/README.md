In this project, I made a coffee machine using Object Oriented Programming.

Program reads one option from the standard input, which can be "buy", "fill", "take", "remaining" and "exit". If a user wants to buy some coffee, the input is "buy". If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".
If the user writes "buy" then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
    For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
    For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.
Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.

If the user writes "fill", the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.
If the user writes "take" the program should give all the money that it earned from selling coffee.
If user types "exit" then he can exit through the program and if he types "remaining" then he can get remaining data of coffee machine.
At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
Program that will work endlessly to make coffee for all interested persons until the shutdown signal is given.

