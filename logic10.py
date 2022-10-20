def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return ( (a>=10 and 100>=a) or  (a>=-100 and a<=-10) and a%1==0)

print(main(50))



