
'''
Problem Description:

Write a recursive program to calculate the harmonic sum of the first n numbers.
'''
def harmonic_sum(n):
    '''n = Input in integer format
       output:return harmonic sum'''
    if n<=1:
        return 1
    return format((1/n + float(harmonic_sum(n-1))),".3f")

    # YOUR CODE GOES HERE
print(harmonic_sum(7))