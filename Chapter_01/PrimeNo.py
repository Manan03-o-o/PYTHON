def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input("Start: "))
b = int(input("End: "))

for i in range(a, b+1):
    if is_prime(i):
        print(i, end=" ")
        # print(i)  # Alternative way to print each prime on a new line
print()  # For a new line after printing all primes
# This program prints all prime numbers in the given range [a, b].
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# For example, 2, 3, 5, 7, 11,
# and 13 are prime numbers, while 4, 6, 8, 9, and 10 are not.
# The program defines a function is_prime to check if a number is prime.
# It then takes two inputs from the user to define the range and prints all prime numbers within that range.
# The program uses a loop to iterate through each number in the specified range and calls the is_prime function to check for primality.
