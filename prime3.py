Number = int(input("Enter a non-negative Integer:"))
lower = 2
upper = Number

def isrange_prime():
    print("Prime numbers between" ,lower, "and %d are :\n"  % upper)
    for num in range (lower, upper + 1):
        #prime numbers are greater than one
        if (num > 1):
            for i in range(2, num):
                if (num % i) ==0:
                    break
                else:
                    print(num)

    
     
