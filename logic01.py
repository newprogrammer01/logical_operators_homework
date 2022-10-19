def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    if a<b and b<c:
        return ("True")
    else:
        return ("False")
    if c>b and b>a:
        return ("True")
    else: 
        return ("False")
print(main(3,4,5))






    













   