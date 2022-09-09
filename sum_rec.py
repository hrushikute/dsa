'''
Problem Description:

Write a program to calculate the sum of the positive integers of the series n + (n-2) + (n-4)..... (until n-x ≤0).
'''
def sum_series(n):
    '''n = Input in integer format
       output:return sum of the series'''
    # YOUR CODE GOES HERE
    if n<=0:
        return 0

    return n+sum_series(n-2)

print(sum_series(1000))