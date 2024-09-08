"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples_of_three_or_five(i: int = 0) -> int:
    sum = 0
    for x in range(i):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum


def main() -> int:
    return sum_multiples_of_three_or_five(1000)


if __name__ == "__main__":
    print("Starting Problem 1")
    solution = main()
    print(f"The solution to problem 1 is {solution}")
