def all_primes(start,end):
    list_primes = []
    for i in range(start,end):
        for a in range(2,i):
            if i % a == 0:
                list_primes.append(i)

    return list_primes
