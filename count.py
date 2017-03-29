Number = (input("Please enter a non-negative integer:"))



def digit_count():
    zero_count = 0
    even_count = 0
    odd_count = 0
    global number
    number = int(Number)
    num = number
    while (num > 0):
        if (num % 10 == 0):
            zero_count += 1
        elif (num % 2 == 0):
            even_count += 1
        else:
            odd_count +=1

        num= num // 10
        
    print ("zero_count: %d" %zero_count)
    print ("even_count: %d" % even_count)
    print ("odd_count: %d" % odd_count)
    
print (digit_count() )
