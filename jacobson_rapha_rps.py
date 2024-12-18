#cat
#https://devdojo.com/kmhmubin/build-a-python3-rock-paper-scissor-game-using-ascii-art

import os
import random
import time

print ("Hello!")                                                                                            #display ("Hello")

time.sleep (1)                                                                                              #program pauses for 1 second
 
possible_actions = ["rock", "paper", "scissors"]                                                            #possible actions of what the user can input
rock = '''                                                                                              
         ______
    ---'   ____)  
          (_____)  
          (_____)  
          (____)
    ---.__(___)  
'''                                                                                                         #defines rock ASCII art
paper = ''' 
         ______
     ---'   _____)___
              _______)  
              ________)  
             ________)
    ---.___________)  
'''                                                                                                         #defines paper ASCII art
scissors = '''
        _______
    ---'   ____)____  
              ______)  
           __________)  
          (____)
    ---.__(___) 
'''                                                                                                         #defines scissors ASCII art
action_displays = [rock, paper, scissors]                                                                   #defines variable that lists each of the ASCII arts so it can match up with the user's answer
score_limit = 3

while True:                                                                                                 #forever loop
    p1_score = 0
    p2_score = 0 
    print ()                                                                                                #blank line                                                                              
    user1_name = input ("Player 1, Enter your name: ")                                                      #ask user 1 to input a name which is now the varaible user1_name          
    while True:
        amnt_of_players = input ("Would you like to play with 1 or 2 players?: ")                           #create variable and ask if there are going to be 1 or 2 players

        if amnt_of_players == '1':                                                                          #if user inputs "1"  
            user2_name = "computer"                                                                         #set user2_name to "computer"                    
            break                                                                                           #end forever loop
        elif amnt_of_players == "2":                                                                        #if user inputs "2"
            user2_name = input("Player 2, enter your name: ")                                               #ask user 2 to input a name which is now the varaible user2_name
            break                                                                                           #end forever loop
        else:                                                                                               #if user response is not "1" or "2"                                                
            print ("invalid response - try again")                                                          #display "invalid response - try again"
    
    while p1_score < score_limit and p2_score < score_limit:
        if amnt_of_players == '1':                                                                          #if user inputs "1"  
            user_action_1 = input("Enter a choice ('rock', 'paper', 'scissors') - type 'q' to quit - Game is first to 3: ")    #variable user_action_1 = the answer to the user's input
            if user_action_1 == 'q':
                exit()
            action_2 = random.choice(possible_actions)                                                      #action_2 = computer's random choice of possible actions
        else:                                                                                               #if user inputs "2"
            user_action_1 = input(f"{user1_name}, enter a choice ('rock', 'paper', 'scissors') - type 'q' to quit - game is first to 3: ")  #variable user_action_1 = the answer to the user's input
            if user_action_1 == "q":                                                                        #if user chooses "q"
                exit()                                                                                      #completely end program
            os.system('cls')                                                                                #clear screen
            action_2 = input(f"{user2_name}, Enter a choice (rock, paper, scissors) - type 'q' to quit - game is first to 3: ")  #variable action_2 = the answer to the user's input
            os.system('cls')                                                                                #clear screen
        time.sleep (2)                                                                                      #program pauses for 2 seconds
        print(f"\n {user1_name} chose {action_displays[possible_actions.index(user_action_1)]} {user2_name} chose {action_displays[possible_actions.index(action_2)]}\n") #displays what the user 1 and what user 2 chose in ASCII art

        if user_action_1 == action_2:                                                   #if user picked the same action as computer
            print(f"Both players selected {user_action_1}. It's a tie!")                #display "Both players selected___. it's a tie"
        elif user_action_1 == "rock":                                                   #elif user action = rock            
            if action_2 == "scissors":                                                  #if computer chooses scissors
                print(f"Rock beats scissors!{user1_name} wins!")                        #display "Rock beats scissors! You win!"
                p1_score+=1
            elif action_2 == "paper":                                                   #if computer action is paper 
                print(f"Paper covers rock! {user2_name} wins!")                         #display "Paper covers rock! You lose."
                p2_score+=1
        elif user_action_1 == "paper":                                                  #elif user action = paper
            if action_2 == "rock":                                                      #if computer chooses rock
                print(f"Paper covers rock! {user1_name} wins!")                         #display "Paper covers rock! You win!"
                p1_score+=1
            elif action_2 == "scissors":                                                #if computer action is scissor
                print(f"Scissors cuts paper! {user2_name} wins!")                       #display "Scissors cuts paper! You lose."
                p2_score+=1
        elif user_action_1 == "scissors":                                               #elif user action = scissors
            if action_2 == "paper":                                                     #if computer chooses paper
                print(f"Scissors cuts paper! {user1_name} wins!")                       #display "Scissors cuts paper! You win!"
                p1_score+=1
            elif action_2 == "rock":                                                    #if computer chooses rock
                print(f"Rock beats scissors! {user2_name} wins!")                       #display "Rock beasts scissors! You lose." 
                p2_score+=1
        else:                                                                           #if user inputs anything but "rock", "paper", "scissors", or "q"
            print ("invalid responses - try again")                                     #display "invalid responses - try again"
        
        if p1_score == 3:                                                               #if player 1 has 3 points                                        
            print (f"{user1_name} wins all 3 rounds!")                                  #display "(player 1's name) wins!"
            break                                                                       #end forever loop
        elif p2_score == 3:                                                             #if player 1 has 3 points
            print (f"{user2_name} wins all 3 rounds!")                                  #display "(player 2's name) wins!"
            break                                                                       #end forever loop
        else:                                                                           #if neither player has reached 3 points yet
            print (f"{user2_name} has {p2_score} point(s). {user1_name} has {p1_score} point(s).") #display each player's score