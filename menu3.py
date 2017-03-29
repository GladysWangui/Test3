#dont be shocked by the way its written..kimalamala

import sys, os

global Number


menu_actions  = {}  
global number
 

 
# Main menu
def main_menu():
    os.system('clear')
    
    print("-"*80)    
    print ("Please select from the following Menu Choices to start:")
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    print("-"*80)    

    choice = input(" >>  ")
    exec_menu(choice)
 
    return
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

def inp_number():
    print ("Welcome to Integer Fun!!\n")
             
    Number = int(input("Enter a non-negative number please: "))
    #number = Number
    #if (number < 0):
     #   print("Sorry  %d  is not a non-negative Integer.\n" %number )
    #elif(number ==''):
     #   print("Sorry  cannot be empty")
    #else:    
     #   print ("Great!\n%d is a non-negative Integer.\n" %number)
    return Number
       
 
 
# Menu 1 enter a new number
def new_number():
    print ("Hello Menu 1 !\n")
    print ("You Chose, (1)Enter a new Number!")
    Number = input("Enter a new non-negative number: ") 
    number= int(Number)
    if (number < 0 ):
        print("Sorry  %d  is not a non-negative Integer.\n Try again" %number )
    else:
        print ("Great!\n%d is a positive Number.\n" %number)
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 2 count number of odd,even and zeros in the number
def digit_count():
    number = Number
    print ("Hello Menu 2 !\n")
    zero_count = 0
    even_count = 0
    odd_count = 0
    num= 4
    count = [int(i) for i in number] # count all zeros including leading zeros

    for i in count:
        if i == 0:
            zero_count += 1
        elif i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return zero_count, even_count, odd_count


    zero_count, even_count, odd_count = digit_count(count)
    print ('The odd/even count for',number,'=>')
    print('Zero Count: %d' % zero_count)
    print('Even Count: %d' % even_count)
    print('Odd Count: %d' % odd_count)
    print ("5. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return
# Menu 3 determine number of prime numbers btwn 2 and the number
def is_prime():
    print ("Hello Menu 3 !\n")
    print ("5. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 4 sum of the digits of the number
def Sum_Of_Digits():
    global number
    number = num
    print ("Hello Menu 4 !\n")
    Sum = 0
    while(number > 0):
        Reminder = number % 10
        Sum = Sum + Reminder
        number= number //10
    return Sum

    Sum = Sum_Of_Digits(number)
    print("\nThe Sum of the digits of the Given Number(",number,") = %d" %Sum)
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return


 
# Exit program
def exit():
    print ('......GOODBYE......')

    sys.exit()
 

 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': new_number,
    '2': digit_count,
    '3': is_prime,
    '4': Sum_Of_Digits,
    '5': exit,
}
 
 
#main



if __name__ == "__main__":
    
    inp_number()
       
    main_menu()




 
