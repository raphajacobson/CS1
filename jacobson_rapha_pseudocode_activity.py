import random

name = input ("What's your name?: ")                                                      #name = question "what's your name"
print (f"good luck {name}")                                                               #display "good luck (name)"
words = ["computer", "programming", "python", "logic", "board", "game", "condition"]      #words = list of computer, programming, python, logic, board, game, condition
games = 0                                                                                 #set games to 0
wins = 0                                                                                  #set wins to 0

while True:                                                                               #forever loop
    word = random.choice(words)                                                           #word = random choice of words
    display = list(word)                                                                  #display = make a list of what you set for the word
    random.shuffle(display)                                                               #random shuffle display to mix it up
    display = "".join(display)                                                            #display = join display to make scrambled word
    turns = 5                                                                             #set turns to 5

    while turns > 0:                                                                      #while turns is greater than 0
        guess = input(f"unscramble {display}. Enter real word here: ")                    #guess = question "unscramble (display) enter the real word here: "

        if guess == word:                                                                 #if user guess is my word
            print ("You got it!")                                                         #display "you got it!"
            wins+=1                                                                       #plus 1 win
            break                                                                         #end forever loop
        while True:                                                                       #forever loop
            scramble = input (f"You did not get my word. you have {turns} tries left. Would you like to rescramble?: ") #scramble = question "you did not get my word. would you like to rescramble? y or n: "
           
            if scramble == "n":                                                           #if user chooses n
                break                                                                     #end forever loop
            elif scramble == "y":                                                         #else if user chooses y
                display = list(word)                                                      #display = make list from word
                random.shuffle(display)                                                   #randomly shuffle my list
                display = "".join(display)                                                #display = join list together
                break                                                                     #end forever loop
            else:                                                                         #else
                print ("Invalid response")                                                #display "invalid response"
        turns-=1                                                                          #take 1 away from turns
    print (f"The word was {word}")                                                        #display "the word was (word)"
    games+=1                                                                              #add 1 to games

    while True:                                                                           #forever loop
        play_again = input (f"{name}, you have {wins} wins out of {games} games. It took you {turns} tries. Do you want to play again? y or n: ") #play again = question "(name), you have (wins) wins out of (games) games. It took you (turns) tries. Do you want to play again? y or n: "
       
        if play_again == "n":                                                             #if user chooses n
            exit()                                                                        #exit
        elif play_again == "y":                                                           #else if user chooses y
            break                                                                         #end forever loop
        else:                                                                             #else
            print ("Invalid response. Limited to y or n.")                                #print "Invalid response. Limited to y or n"




