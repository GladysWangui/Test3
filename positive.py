num = int(input(" Please enter a non-negative Integer:"))

if (num < 0 ):
    print("Sorry  %d  is not a non-negative Integer.\n Try again" %num )

    num = int(input(" Please enter a non-negative Integer:"))
    

else:
    print ("Great!\n %d is a positive Number.\n"
           "To Continue Please select from the following Menu Choices. " %num)



