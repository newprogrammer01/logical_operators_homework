def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """

    return (100<=a<1000 and a%1==0) or (-1000<a<=-100 and a%1==0)
print(main(-620))
