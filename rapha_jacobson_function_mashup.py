import random

def chorus():
    '''
    Prints chorus of a song
    Args:
        None
    Returns:
        Print: Chorus
    '''
    print("all round the town")
def sing_song():
    '''
    Sings entire song using chorus function
    Args:
        None
    Returns:
        Print: entire song
    '''
    print("The wheels on the bus go round and round")
    print("Round and round Round and round")
    print("The wheels on the bus go round and round")
    chorus()
    print("The wipers on the bus go swish, swish, swish")
    print("swish, swish, swish")
    print("swish, swish, swish")
    print("The wipers on the bus go swish, swish, swish")
    chorus()
    print("The horn on the bus goes beep, beep, beep")
    print("beep, beep, beep")
    print("beep, beep, beep")
    print("The horn on the bus goes beep, beep, beep")
    chorus()
    print("The parents on the bus go shush, shush, shush")
    print("shush, shush, shush")
    print("shush, shush, shush")
    print("The parents on the bus go shush, shush, shush")
    chorus()



def add(x, y):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of the two numbers
    '''
    print("we are adding the 2 numbers...")
    print(x+y)

def print_list(array):
    '''
    Takes a list and prints every element in that list individually
    Args:
        array (list): A given list
    Returns:
        print: Every item in given list vertically
    '''
    for i in array:
        print(i)

def in_list(element, lst):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        element: Any given element
        lst: Any given list
    Returns:
        print (bool): If the inputted element is in the inputted list
    '''
    return element in lst

def is_integer(parameter):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        paramater: Any given paramater
    Returns:
        print (bool): If the inputted element is an integer
    '''
    try:
        int(parameter)
        return True
    except ValueError:
        return False
    
def get_integers():
    '''
    Asks the user for two numbers, makes sure they are integers using is_integer function, and then prints the two integers
    Args:
        None
    Returns:
        print: The two numbers inputted if and only if they are integers
    '''
    while True:
        number1 = input("enter any number: ")
        number2 = input("enter another number: ")
        
        if is_integer(number1) and is_integer(number2):
            return int(number1), int(number2)

def get_random():
    '''
    Uses get_integers function to get 2 numbers and make sure they are integers and then prints a random number in between the two given integers
    Args:
        None
    Returns:
        print: Any number between the two inputted numbers
    '''
    number1, number2 = get_integers()
    print(random.randint(number1, number2))

def count_vowels(strng):
    '''
    Takes in a string and then prints the number of vowels in it
    Args:
        strng (string): any given word
    Returns:
        print: The number of vowels in the string
    '''
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for vowel in strng:
        if vowel.lower() in vowels:
            count += 1
    return count

def get_initials(full_name):
    '''
    Takes in a name and then prints its initials
    Args:
        full_name (string): Any given first and last name
    Returns:
        print: The initials of the inputted name
    '''
    names = full_name.split()
    initials = ""
    for name in names:
        initials += name[0].upper()
    return initials
    
def reverse_string(strng):
    '''
    Takes in a string and then prints it backwards
    Args:
        strng (string): any given word
    Returns:
        print: The inputted string backwards
    '''
    return strng[::-1]

def is_palindrome(strng):
    '''
    Takes in a string and prints a boolean value whether or not it is a palindrome
    Args:
        strng (string): any given word
    Returns:
        print: True of false is the word is a palindrom
    '''
    return strng == reverse_string(strng)

def generate_name(firstnames, lastnames):
    """
    Generates a random full name using separate lists for first and last names
    Args:
        None
    Returns:
        Print: Random first and last name
    """
    return f"{random.choice(firstnames)} {random.choice(lastnames)}"

def main():
    while True:
        option = input("which function would you like to run? 1-12?: ")
        
        if option == "1":
            sing_song()
        elif option == "2":
            a, b = get_integers()
            add(a, b)
        elif option == "3":
            user_list = input('Enter any list of items (use spaces between each item) and we will print all of the items: ').split(' ')
            print_list(user_list)
        elif option == "4":
            user_list = input('Enter any list of items (use spaces between each item): ').split(' ')
            check = input('Enter any word and we will tell you if it is in the list you just created: ')
            print(in_list(check, user_list))
        elif option == "5":
            check = input('Enter anything and we will tell you if it is an integer: ')
            print(is_integer(check))
        elif option == "6":
            get_random()
        elif option == "7":
            phrase = input('Enter a word or phrase and we will count the number of vowels in it: ')
            print(count_vowels(phrase))
        elif option == "8":
            name = input('Enter a name and we will calculate its initials: ')
            print(get_initials(name))
        elif option == "9":
            word = input("enter any word and we will spell it backwards: ")
            print(reverse_string(word))
        elif option == "10":
            palindrome = input("Enter any word and we will tell you if it is a palindrome: ")
            print(is_palindrome(palindrome))
        elif option == "11":
            firstnames = input("enter a list of first names (with a space in between each): ").split(' ')
            lastnames = input("enter a list of last names (with a space in between each): ").split(' ')
            print("hold on while we generate a random name from your lists.")
            print(generate_name(firstnames, lastnames))
        else:
            print ("invalid response - try again")

main()

        
