'''
Author: Rapha Jacobson

Description: Asks user to input passwords and the program stores them. The program can delete passwords, changes, passwords, access passwords, generate passwords, export passwords to a spreadsheet, and check the security of passwords.

Challenges:
1.Allow the user to retroactively add more usernames and passwords
2. Allow the user to change usernames and passwords
3. Store the list of websites with usernames and passwords in an excel spreadsheet
4. Require a password to enter the password keeper
5. Generate a secure password for the user
6. heck how complex/secure the passwords are
7. Delete a password

Sources: Marciano google slides, Marciano CSV code
'''

import csv
import time
import os
import random

def enter_keeper(secret_code, tries):
    """
    Asks user to create a secret password in order to enter password keeper

    Args:
        secret_code = the password that the user enters
        tries = Amount of tries to try password before not able to enter password keeper

    Returns:
        The password the user inputs
    """
    for i in range(tries):
        keeper_password = input ("Enter the secret code for your password keeper: ")
    
        if keeper_password == secret_code:
            print ("Your're in!")
            time.sleep(1)
            os.system('cls')
            return True
        print (f"Incorrect. You have {tries-i-1} tries left")
    return False
def find_index(websites):
    """
    Finds the index of any item in any list

    Args:
        Website(list) = Any website

    Returns:
        The index of the given websites' index in usernames and passwords
    """
    while True:
        web = input("Enter the website: ")

        if web in websites:
            return websites.index(web)
        else:
            print ("That website is not in password keeper. Try again.")
def add_entry(websites, usernames, passwords):
    """
    Ask user for a website, username, and password and store them in password keeper

    Args:
        Website(list) = Any website
        Username(list) = Any username
        Password(list) = Any password

    Returns:
        Lists filled with the websites, usernames, and passwords just given
    """
    while True:
        website = input("Which website would you like to add (q to stop adding): ")

        if website.lower() == "q":
            break
        
        username = input ("What is the username for that website?: ")
        password = input ("What is the password for that website? (Press 'g' to generate): ")

        if password.lower() == "g":
            password = generate_password()
        websites.append(website)
        usernames.append(username)
        passwords.append(password)
def access_pwd(website, username, password):
    """
    Ask user for a website and prints that website’s username and password

    Args:
        Website(str) = Any website already stored

    Returns:
        The username and password of the inputted website
    """

    print(f'''
Website: {website}
Username: {username} 
Password: {password}
    ''')
def print_all_pwds(websites, usernames, passwords):
    """
    Prints everything stored in password keeper

    Args:
        None

    Returns:
        All websites, usernames, and passwords stored in password keeper
    """
    for i in range (len(websites)):
        access_pwd(websites[i], usernames[i], passwords[i])
def export_to_csv(filename, headers, *arrays):
    """
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    """
    if not arrays:                                                          #If there is no inputted data
        raise ValueError("At least one array must be provided.")            #Dont allow to continue because there must be some data
    
    num_rows = len(arrays[0])                                               #The number of rows is equal to the amount of arrays

    for arr in arrays:                                                      #for loop
        if len(arr) != num_rows:                                            #If the amount of arrays does not equal the amount of rows
            raise ValueError("All arrays must have the same length.")       #Dont allow because the maount of rays must equal the amount of rows
    
    with open(filename, 'w', newline='') as csvfile:                        #Opens new csv file
        csvwriter = csv.writer(csvfile)                                     #Inputs data into csv file
        csvwriter.writerow(headers)                                         #Writes the headers into the csv file

        for i in range(num_rows):                                           #for loop
            row = [arr[i] for arr in arrays]                                #In one row print all of the data from one array's index
            csvwriter.writerow(row)                                         #Insert the rows into the csv file
def change_entry(websites, usernames, passwords):
    """
    Allows user to change a website, username, or password

    Args:
        Website(list) = Any website
        Username(list) = Any username
        Password(list) = Any password

    Returns:
        The  website with its new matching username and password
    """
    change_entry_entry_index = find_index(websites)
    websites[change_entry_entry_index] = input('Enter new website: ')
    usernames[change_entry_entry_index] = input('Enter new username: ')
    password = input('Enter new password (press "g" to generate): ')

    if password.lower() == "g":
        password = generate_password()
    else:
        print('Checking your password security...')
        length = get_password_length()
        check_security(password, length, True)
    passwords[change_entry_entry_index] = password
def delete_entry(websites, usernames, passwords):
    """
    Ask user for a website, username, and password and deletes them from password keeper

    Args:
        Website(list) = Any website already stored
        Username(list) = Any username already stored
        Password(list) = Any password already stored

    Returns:
        Lists filled without the websites, usernames, and passwords just given
    """
    delete_entry_index = find_index(websites)
    websites.pop(delete_entry_index)
    usernames.pop(delete_entry_index)
    passwords.pop(delete_entry_index)
def get_password_length():
    """
    Asks user to give their desired length of a randomely generated password

    Args:
        None

    Returns:
        The length which the user wants to have their generated password
    """
    while True:
        try:
            length = int(input("insert the desired length for your password: "))

            if length > 3:
                return length
            else:
                print('Length must be at least 4')
        except ValueError:
            print ("not an integer - try again")
def generate_password():
    """
    Randomly generates a password for the user with the length prompted by the user

    Args:
        None

    Returns:
        The randomely generated password
    """
    length = get_password_length()
    
    while True:
        pwd = ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'), length))

        if check_security(pwd, length, False):
            return pwd
def check_security(pwd, length, display):
    """
    Checks the strength of any given password

    Args:
        pwd = password inputted by user
        length(int) = length of pwd
        display(bool) = Whether or not the security will be printed

    Returns:
        Whether or not the password is secure
    """
    if len(pwd) < length or pwd.lower() == pwd or pwd.upper() == pwd or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list('`~!@#$')):
        if display:
            print(f'{pwd} is not secure')
        return False
    else:
        if display:
            print(f'{pwd} is secure')
        return True
def clear_console(delay):
    time.sleep(delay)
    os.system('cls')
def main():
    websites = []
    usernames = []
    passwords = []

    secret_code = input("Enter your secret code to begin password keeper (Press 'g' to generate): ")

    if secret_code.lower() == "g":
        secret_code = generate_password()
        print(f'Your generated secret code is {secret_code}')
        clear_console(5)
    clear_console(1)
    add_entry(websites, usernames, passwords)
    clear_console(1)

    if not enter_keeper(secret_code, 3):
        print("You failed to enter!")
        clear_console(1)
        exit()

    while True:
        print('''which option would you like to choose? (Enter "q" to quit)
1. Add a password
2. Get a password
3. Show all passwords
4. Change a website, username, or password
5. Delete a password
6. Export all websites, usernames, and passwords to a spreadsheet
7. Generate a password
8. Check the security of a password
        ''')
        choice = input("enter the number you would like to choose: ").lower()

        if choice == "q":
            break
        elif choice == "1":
            add_entry(websites, usernames, passwords)
        elif choice == "2":
            index = find_index(websites)
            access_pwd(websites[index], usernames[index], passwords[index])
        elif choice == "3":
            print_all_pwds(websites, usernames, passwords)
        elif choice == "4":
            change_entry(websites, usernames, passwords)
        elif choice == "5":
            delete_entry(websites, usernames, passwords)
        elif choice == "6":
            export_to_csv("data.csv", ["website", "username", "password"], websites, usernames, passwords)
        elif choice == "7":
            print(f'Your generated password is: {generate_password()}')
        elif choice == "8":
            pwd = input('Enter a password to check or "p" to see a specific password from your list of websites: ')

            if pwd.lower() == "p":
                index = find_index(websites)
                pwd = passwords[index]
            length = get_password_length()
            check_security(pwd, length, True)
        else:
            print("Invalid response - try again")
main()