def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    
    i = n-1
    o = n
    
    if k>0:
        while i>(n-k):
            o = o*i
            i -= 1
    elif k==0:
        o = 1

    return o



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0 
    for i in range(0, len(str(y))):
        sum = sum + int(str(y)[i])
    return(sum) 



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # if only one digit, return false
    if len(str(n))<2:
        return False
    
    # if at least two digits, perform below
    else:
        total, i = 0, 1
        while i < len(str(n)) and total != "88":
            total = str(n)[i-1] + str(n)[i]
            i += 1

        return total == "88"


