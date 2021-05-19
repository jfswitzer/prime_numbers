# Program to check if a number is prime or not
# from https://www.programiz.com/python-programming/examples/prime-number
def is_prime(num):
    if num < 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
nums = [x for x in range(50000)]
prime = [is_prime(n) for n in nums]
print(prime)
