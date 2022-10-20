def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return((a<=-10 and a>-100 and a%2==0)  or (a>=10 and 100>a  and a%2==0))

print(main(25))
