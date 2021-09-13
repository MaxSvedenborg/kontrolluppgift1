# 4. Write a Python function to solve the Fibonacci sequence using recursion

data = 20


def recursive_fibonacci(x):
    """If the data is less or equal to one, then we return and print it(not needed but printing for clarification),
       else, we subtract the number we are on -1 to get previously number and add it to the previous number
       before that as the fibonacci sequence is the number + the previous number in sequence.
    """
    if x <= 1:
        return x
    else:
        return recursive_fibonacci(x - 1) + recursive_fibonacci(x - 2)


for y in range(data):
    print(recursive_fibonacci(y))




