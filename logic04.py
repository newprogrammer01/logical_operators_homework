def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    c=a%2
    d=a%2
    if c>0 and d>0:
       return ("False")
    if c==0 and d==0:
        return ("True")
print(main(5,4))
