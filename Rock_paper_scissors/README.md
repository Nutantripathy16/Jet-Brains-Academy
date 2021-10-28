About The Program
This  is a program for extended version of rock, paper and scissors game and along with rock paper and scissors we have around 12 other options so in total we have 15 options in game.
Extended versions of the game will decreasing the probability of a draw, so it could be cool to play them.
At this stage, before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma. For example,rock,paper,scissors,snake,sponge
If the user inputs an empty line, this program will start the game with default options: rock, paper, and scissors.
Total options along with rock, paper and scissors are :- rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
After the game options are defined, program will output "Okay, let's start".
Whatever list of options the user chooses, this program will identify which option beats which, that is, the relationships between different options.
So First, every option is equal to itself (causing a draw if both the user and the computer choose the same option). Secondly, every option wins over one half of the other options of the list and gets defeated by another half.

Objectives For The Program are as follows:-

Output a line for user, Enter your name: . Note that the user will enter his/her name on the same line (not the one following the output!)
Read input specifying the user's name and output a new line Hello, <name>
Read a file named rating.txt and check if there's a record for the user with the same name; if yes, use the score specified in rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting the user's score from 0.
Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
Output a line Okay, let's start
Play the game by the rules defined in the previous stages:
Read the user's input
If the input is !exit, output Bye! and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
Lose -> Sorry, but the computer chose <option>
Draw -> There is a draw (<option>)
Win -> Well done. The computer chose <option> and failed
For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
If the input corresponds to anything else, output Invalid input
Play the game again (with the same options that were defined before the start of the game)
