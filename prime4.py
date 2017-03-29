Number = int(input("Enter a non-negative Integer:"))
lower = 2
upper = Number
print("Prime numbers between" ,lower, "and %d are :\n"  % upper)
for num in range (lower, upper + 1):
    if all(num%i!=0 for i in range(2,num)):
        print (num)
                
