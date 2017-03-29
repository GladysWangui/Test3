Number = int(input(" Please Enter any number:"))
Sum = 0

while(Number > 0):
    Remainder = Number % 10
    Sum = Sum + Remainder
    Number = Number //10

print("\n The Sum of the digits of the Given Number = %d" %Sum)    
