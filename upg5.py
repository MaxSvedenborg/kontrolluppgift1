# 5. Write a Python function to get the sum of a non-negative integer.

data1, data2, = 45, 345

def sum_split_calc(x):
    """
    using the mapfunction that is builtin python, to iterate the given datas each int or string element and using
    the builtin function sum on the result which gives us a split-like function with sum.
    """
    x = map(int,str(x))
    return sum(x)


print(sum_split_calc(data1))
print(sum_split_calc(data2))
