def digit_count(digits):
    """ Takes a list of single digits and returns the 
        count of zeros, evens and odds
    """
    zero_count = 0
    even_count = 0
    odd_count = 0
    for i in digits:
        if i == 0:
            zero_count += 1
        elif i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return zero_count, even_count, odd_count

inp = input("Enter a ten-digit number please: ")
digits = [int(i) for i in inp] # see comment at the bottom of the answer

zero_count, even_count, odd_count = digit_count(digits)

print('zero_count: %d' % zero_count)
print('even_count: %d' % even_count)
print('odd_count: %d' % odd_count)
