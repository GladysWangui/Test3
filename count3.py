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

Number = input("Enter a non-negative number please: ")
num = [int(i) for i in Number] # count all zeros including leading zeros

zero_count, even_count, odd_count = digit_count(num)

print('Zero Count: %d' % zero_count)
print('Even Count: %d' % even_count)
print('Odd Count: %d' % odd_count)
