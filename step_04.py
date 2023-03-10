"""
Step 04.
What about recursive functions?
"""


def fibonacci(nth_term):
    """
    Calculate the nth term in the Fibonacci sequence, starting with n = 0.

    The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... .

    :param nth_term: a positive integer
    :precondition: nth_term is a positive integer
    :postcondition: calculates the nth_term in the Fibonacci sequence
    :return: the nth Fibonacci integer
    """
    if nth_term == 0 or nth_term == 1:
        return_value = 1
    else:
        return_value = fibonacci(nth_term - 1) + fibonacci(nth_term - 2)
    return return_value


def main():
    """
    Drive the program.
    """
    print(fibonacci(5))


if __name__ == "__main__":
    main()
