def rev(n, temp=''):
    ''' n-indicates the number to be reversed,
         output:Return the number in reversed order in the string format'''
    n=str(n)
    # YOUR CODE GOES HERE
    if len(n)<=1:
        return n
    return rev(n[1:]) + n[0]
print(rev(1))