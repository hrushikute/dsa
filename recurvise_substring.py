def countHi(s, count=0):
    ''' s-indicates the string,
         output:Return the count of occurrences of "hi" in s'''
    # YOUR CODE GOES HERE

    # Base case
    len_of_s = len(s)
    # print(s,len_of_s)
    len_of_hi = 2
    if len_of_s < len_of_hi:
        return 0
    # If found increment
    elif s[0:len_of_hi] == "hi":
        return countHi(s[1:])+1

    else:
        return countHi(s[1:])

print(countHi("hiphophip"))

