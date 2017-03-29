import sys, os


menu_actions  = {}

global number

number = 0

# Main menu
def main_menu():
    os.system('clear')

    print ("Please select from the following Menu Choices to start:")
    print ("1. Add a number to the list/array")
    print ("\n2. Display the mean")
    print ("3. Display the median")
    print ("4. Print the list/array to the screen")
    print ("5. Print the list/array in reverse order")
    print ("\n6. Quit \n\n")

    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

#first user input prompt
def add_number():
    print ("Hi There!\nWelcome to Integer Fun!!\n")

    Number = input("Enter a non-negative number please: ")
    global number
    number= int(Number)
    while number:
        if(number >= 0):
            print ("Great!\n%d is a non-negative Number.\n" %number)
            break
    
        elif (number < 0 ):
            print("Sorry  %d  is not a non-negative Integer.\n Try again" %number )
            Number=input("Please Enter a non-negative number: ")
            number= int(Number)
            
    return number
# Menu 1
def menu1():
    print ("Hello Menu 1 !\n")
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
 
# Menu 2
def menu2():
    print ("Hello Menu 2 !\n")
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return
# Menu 3
def menu3():
    print ("Hello Menu 3 !\n")
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return
# Menu 4
def menu4():
    print ("Hello Menu 4 !\n")
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Exit program
def exit():
    print ('Have a Good Day! \n.....BYE ..BYE !......')

    sys.exit()


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': inp_number,
    '2': menu1,
    '3': menu2,
    '4': menu3,
    '5': menu4,	
    '6': exit,
}


#main



if __name__ == "__main__":

    inp_number()
    main_menu()

