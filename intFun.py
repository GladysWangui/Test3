#==========================
#Program which reads in a non-negative integer from the
#user. The user will then be prompted with a
#menu of choices (this menu should be
#repetitively displayed until the user chooses
#to quit
#------------------------


#this are separate functions without the Menu Part

global number

#user prompt to enter a non-negative number
Number = input("Enter a non-negative number please: ")

number= int(Number)
if (number < 0 ): #check if its non-negative
    print("Sorry  %d  is not a non-negative Integer.\n Try again" %number )

else:
    print ("Yaay!!\n%d is a non-negative Number.\n" %number
               #"To Continue Please select from the following Menu Choices. "
               )
    
# count the number of even, odd and zeros in the integer
def digit_count(num):
    zero_count = 0
    even_count = 0
    odd_count = 0
    for i in num:
        if i == 0:
            zero_count += 1
        elif i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return zero_count, even_count, odd_count

num = [int(i) for i in Number] # count all zeros including leading zeros

zero_count, even_count, odd_count = digit_count(num)
print ('The odd/even count for',Number,'=>')
print('Zero Count: %d' % zero_count)
print('Even Count: %d' % even_count)
print('Odd Count: %d' % odd_count)

#sum of all Digits in the number
def Sum_Of_Digits(number):
    Sum = 0
    while(number > 0):
        Reminder = number % 10
        Sum = Sum + Reminder
        number = number //10
    return Sum

Sum = Sum_Of_Digits(number)
print("\nThe Sum of the digits of the Given Number(",number,") = %d" %Sum)

#prime numbers between 2 and the integer
lower = 2
upper = number
print("Prime numbers between" ,lower, "and ",upper," are :\n")
for num in range (lower, upper + 1):
     if all(num%i!=0 for i in range(2,num)):
        print (num)

        
    
        
   


