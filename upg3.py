# 3. Write a Python function of to recursively calculate the sum

data_list = [1, 2, [3,4], [5,6]]


def get_sum(x, self=[]):
    """we check if our given list is an instance of x, and then adds it to a list x.
       then we do the same with x, for every element, which now have created a single list of all elements,
       which can be summarized thanks to pythons builtin sum-function.
    """
    if not isinstance(x, list):
        return self.append(x)

    for y in x:
        get_sum(y, self)

    return sum(self)


print(get_sum(data_list))


