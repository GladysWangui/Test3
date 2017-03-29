#========================================================+
# Program which reads in a non-negative integer from the + 
# user. The user is then be prompted with a              +
# menu of choices (this menu should bin                  + 
# repetitively displayed until the user choose           +
# to quit                                                +   
#--------------------------------------------------------+

import sys, os


menu_actions  = {}

global number

number = 0

# Main menu
def main_menu():
    os.system('clear')

    print("~"*80)
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
def inp_number():
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


# Menu 1 enter a new number
def new_number():
    print ("Hello!\n")
    print ("You Chose,(1)Enter a new Number!")
    Number = input("Enter a new non-negative number: ")
    global number
    number= int(Number)
    while number:
        if(number >= 0):
            print ("Great!\n%d is a non-negative Number.\n" %number)
            break
    
        elif (number < 0 ):
            print("Sorry  %d  is not a non-negative Integer.\n Try again" %number )
            Number=input("Enter a new non-negative number: ")
            number= int(Number)
            
    print("-"*80)    
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    print("-"*80)
    choice = input(" >>  ")
    exec_menu(choice)
    return number

# Menu 2 count number of odd,even and zeros in the number
def digit_count():
    print ("Hello!\n")
    print ("You Chose,(2)Print the number of Odd digits,"
           "Even digits and zeros in the integer!")
    zero_count = 0
    even_count = 0
    odd_count = 0
    global number
    Number = number
    num = number
    while (num > 0):
        if (num % 10 == 0):#zeros count
            zero_count += 1
        elif (num % 2 == 0):#even numbers count
            even_count += 1 
        else: #odd numbers count
            odd_count +=1

        num= num // 10
    print ('The odd/even count for',Number,'=>')
          
    print ("zero_count: %d" %zero_count)
    print ("even_count: %d" % even_count)
    print ("odd_count: %d\n" % odd_count)
    
    
    print("+"*80)
    print ("Please select from the following Menu Choices to Continue or Quit")
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    print("+"*80)
    
    choice = input(" >>  ")
    exec_menu(choice)
    return
    print (digit_count(Number))

# Menu 3 determine number of prime numbers btwn 2 and the number
def is_prime():
    print ("Hello! You Chose, Print the prime numbers between 2 and the integer!\n")
    global number
    lower = 2
    upper = number
    print("Prime numbers between" ,lower, "and %d are :\n"  % upper)

    for num in range (lower, upper + 1):
        if all(num%i!=0 for i in range(2,num)):
            
            print (num)
            
    print("="*80)
    print ("Please select from the following Menu Choices to Continue or Quit")
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    print("="*80)
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 4 sum of the digits of the number
def Sum_Of_Digits():
    global number
    Number = int(number)
    Sum = 0

    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10

    print("\n Sum of the digits of Given Number(",number,") = %d" %Sum)
    print('*'*80)
    print ("Please select from the following Menu Choices to Continue or Quit")
    print ("1. Enter a new Number")
    print ("\n2. Print the number of Odd digits,"
           "Even digits and zeros in the integer")
    print ("3. Print the prime numbers between 2 and the integer")
    print ("4. Print the sum of the digits of the integer")
    print ("\n5. Quit the Program")
    print('*'*80)
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





