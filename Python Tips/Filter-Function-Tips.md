# Extract Prime Numbers in Python

## Overview
This Python script is designed to efficiently extract all prime numbers from a predefined range of integers. It demonstrates the power of Python's built-in functions and efficient programming practices.

## Description
The script starts with a range of numbers from 2 to 1000. The objective is to filter out all the prime numbers within this range. To accomplish this, the script defines a function `is_prime` that checks whether a given number is prime. The function returns `True` if the number is prime and `False` otherwise. We then utilize Python's built-in `filter` function, passing `is_prime` and our range of numbers. This filters out all non-prime numbers, leaving us with a list of primes. Initially, the `filter` function returns a filter object for memory efficiency; however, we convert this into a list to view the prime numbers.

## Code Snippet
```python
nums = range(2, 1000)

def is_prime(num):
    if num < 2:
        return False
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums)) # you can pass custom functions to filter function

print(f"{primes = }")
