# ----------------------------
# TIMEIT AND PERFORMANCE
# ----------------------------
import timeit

print('\nPerformance and Timeit module')
print('----------------------')
# Experiment with sieve of Eratosthenes
# Basically a way to find the prime numbers in a certain range

# list comprehension that runs through 1 to 150
print([x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1])

# second way to calculate the same thing in a different formula:
print([x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])])

# third way to calculate the same thing in a different formula (using lists):
primes = []
for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)
print(primes)

# which one is faster?
# there is a function inside timeit module, called 'timeit'


# defining test functions
def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return 1  # when using timeit function is always necessary to return a value, otherwise won't work


def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return 1


def test3():
    primes1 = []
    for possiblePrime1 in range(2, 151):
        # Assume number is prime until shown it is not.
        isprime1 = True
        for num1 in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isprime1 = False
                break
        if isprime1:
            primes.append(possiblePrime)
    return 1


# printing timestamps of how long each one of the functions took, running 10 cycles of each (number parameter)
print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))

# now we know that 3rd option is faster than the others, even having mode lines of code
