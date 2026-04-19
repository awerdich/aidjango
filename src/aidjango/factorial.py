import math


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    return math.factorial(n)


if __name__ == "__main__":
    print(factorial(5))
