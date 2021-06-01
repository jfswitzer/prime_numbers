# Program to factor large numbers
# from https://www.programiz.com/python-programming/examples/prime-number
def get_factors(num):
    factors = []
    if num < 1:
        return []
    for i in range(2, num):
        if (num % i) == 0:
            factors.append(i)
            factors.append(int(num/i))
    return factors
nums = [x for x in range(20000)]
factors = [get_factors(n) for n in nums]
print(factors)
