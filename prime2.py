Number = int(input("Enter a non-negative Integer:"))
lower = 2
upper = Number

print("Prime numbers between" ,lower, "and %d are :\n"  % upper)

for num in range (lower, upper + 1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        print (num)
                
