import time
import datetime
def print_colored_text(text, color_name):
    colors = {                                                                                          #different colors able to be used for colored text
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')                                             #default to white if color not found
    print(f"{color_code}{text}\033[0m")                                                                 #print text with color and reset

clock = 630                                                                                             #set clock to 6:30
print ()                                                                                                #blank line
print ()                                                                                                #blank line
print_colored_text ("ALARM!", 'red')                                                                    #display message "ALARM!" using print colored text function to make red text
current_time = datetime.datetime(2024, 10, 21, 6, 30, 0)                                                #set current time to 6:30 AM
print ()                                                                                                #blank line
print_colored_text (current_time.strftime("%H:%M:%S"), 'cyan')                                          #print current time in cyan text
time.sleep(1)                                                                                           #program puases for 1 second
print ()                                                                                                #blank line
while True:                                                                                             #forever loop
    snooze = input ("\nsnooze? y/n: ")                                                                  #ask if user wants to snooze

    if snooze == "y":                                                                                   #if user input is yes
        print ("go back to sleep for 5 mins")                                                           #display message "go back to sleep for 5 mins"
        time.sleep (1)                                                                                  #program puases for 1 second
        current_time += datetime.timedelta(minutes=5)                                                   #add five minutes ot current time
        print ("zzz")                                                                                   #display message "zzz"
        time.sleep (1)                                                                                  #program puases for 1 second
    elif snooze == "n":                                                                                 #if user input is no
        print ("get up")                                                                                #display mesage "get up"
        break                                                                                           #end forever loop
    else:                                                                                               #if user input is anyting other than "y" or "n"
        print ("invalid reponse")                                                                       #display message "invalid reponse"

print ()                                                                                                #blank line
print_colored_text (current_time.strftime("%H:%M:%S"), 'cyan')                                          #display current time in cyan text
print ()                                                                                                #blank line
time.sleep (1)                                                                                          #program pauses for 1 second

while True:                                                                                             #forever loop
    shower = input ("shower? y/n: ")                                                                    #ask if user wants to shower

    if shower == "y":                                                                                   #if user input is yes
        print ("get in shower")                                                                         #display message"get in shower"
        time.sleep (1)                                                                                  #program pauses for 1 second
        print ("brush hair")                                                                            #display message "brush hair"
        time.sleep (1)                                                                                  #program pauses for 1 second
        print ("get out of shower")                                                                     #display message "get out of shower"
        time.sleep (1)                                                                                  #program pauses for 1 second
        print ("brush teeth")                                                                           #display message "brush teeth"
        current_time += datetime.timedelta(minutes=30)                                                  #program pauses for 1 second
        break                                                                                           #end forever loop
    elif shower == "n":                                                                                 #if user input is no 
        print ("brush teeth")                                                                           #display message "brush teeth"
        break                                                                                           #end forever loop
    else:                                                                                               #if user input is anyting other than "y" or "n"
        print ("invalid response")                                                                      #display message "invalid response"
        
print ()                                                                                                #blank line
print_colored_text (current_time.strftime("%H:%M:%S"), 'cyan')                                          #display current time in cyan text
print ()                                                                                                #blank line
time.sleep (1)                                                                                          #program pauses for 1 second

while True:                                                                                             #forever loop
    weather = input ("Is it hot? y/n: ")                                                                #ask user if it is hot

    if weather == "y":                                                                                  #if user input is yes
        print ("put on collared shirt and skirt")                                                       #display message "put on collared shirt and skirt"
        time.sleep (1)                                                                                  #program pauses for 1 second
        print ("walk downstairs")                                                                       #display message "walk downstairs"
        break                                                                                           #end forever loop
    elif weather == "n":                                                                                #if user input is no
        print ("put on jeans and sweater")                                                              #display message "put on jeans and  sweater"
        time.sleep (1)                                                                                  #program pauses for 1 second
        print ("walk downstairs")                                                                       #display message "walk downstairs"
        break                                                                                           #end forever loop
    else:                                                                                               #if user inupt is anything other than "y" or "n"
        print ("invalid response")                                                                      #display message "invalid response"
        
current_time += datetime.timedelta(minutes=20)                                                          #add 20 minutes to current time
print ()                                                                                                #blank line
print_colored_text (current_time.strftime("%H:%M:%S"), 'cyan')                                          #print curent time in cyan

time.sleep (1)                                                                                          #program pauses for 1 second
print ()                                                                                                #blank line

while True:                                                                                             #forever loop
    breakfast = input ("Breakfast? y/n: ")                                                              #ask user if they want breakfast

    time.sleep (1)                                                                                      #program pauses for 1 second    
    if breakfast == "y":                                                                                #if user input is yes
        print ("eat breakfast")                                                                         #display message 
        current_time += datetime.timedelta(minutes=10)                                                  #add ten minutes to current time
        break                                                                                           #end forever loop
    elif breakfast == "n":                                                                              #if user input is no
        print ("eat breakfast later")                                                                   #display message "eat breakfast later"
        break                                                                                           #end forever loop
    else:                                                                                               #if user inupt is anything other than "y" or "n"
        print ("invalid response")                                                                      #display message "invalid response"

if current_time.time() > datetime.time(7,25):                                                           #if current time is after 7:25
        print_colored_text ("You're late! Hurry up!", 'red')                                            #display message "You're late! Hurry up!" in red text"

time.sleep (1)                                                                                          #program pauses for 1 second
print ("go to school")                                                                                  #display message "go to school"


time.sleep (1)                                                                                          #program pauses for 1 second
print ()                                                                                                #blank line
print ("enjoy your day!")                                                                               #display message "enjoy your day!"
time.sleep (1)                                                                                          #program pauses for 1 second
print ()                                                                                                #blank line
print_colored_text("3:00:00 PM", 'cyan')                                                                #display message "3:00 PM" in cyan text
print ()                                                                                                #blank line
time.sleep (1)                                                                                          #program pauses for 1 second
print ("leave school")                                                                                  #display message "leave school"
time.sleep (1)                                                                                          #program pauses for 1 second    
print ()                                                                                                #blank line
print_colored_text ("10:00:00 PM", 'cyan')                                                              #display message "10:00 PM" in cyan text
print ()                                                                                                #blank text
time.sleep (1)                                                                                          #program pauses for 1 second
print ("sleep again")                                                                                   #display message "sleep again"
time.sleep (1)                                                                                          #program pauses for 1 second
print ("zzz")                                                                                           #display message "zzz"
time.sleep (8)                                                                                          #program pauses for 8 seconds


               
                
