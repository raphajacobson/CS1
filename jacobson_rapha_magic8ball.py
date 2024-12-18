import random
import time

possible_computer_actions = ["YES!", "Possibly", "Probably not", "No."]                                 #possible actions the computer can choose                                                                                                       
question_words = ["Am","Do", "Does", "Did", "Is", "Are", "Was", "Were", "Have", "Has", "Had", "Can", "Could", "Should", "Would"]       #create variable quetsion_words

while True:                                                                                             #forever loop
    user_action = input("Ask Magic 8 ball a question: ")                                                #prompt user to ask a question
    user_action_list = user_action.split()                                                              #make a list out of the user's response
    user_question_word = user_action_list[0]                                                            #user_question_word specifies the question word the user inputed
    if "?" not in user_action or user_question_word not in question_words:                              #if there is not "?" in user's response or if there is not a question word
        print ("Try again. 8 Ball can't process.")                                                      #print "Try again. That's not a question."
    else:                                                                                               #if there is a "?" in user's response"
        time.sleep (2)                                                                                  #pause program for 2 seconds
        print(random.choice(possible_computer_actions))                                                 #print computers choice
        break                                                                                           #end forever loop