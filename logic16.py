def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (10_000<=a and a<100_000 and a%1==0) or (-100000<a and a<=-10000 and a%1==0)

print(main(12345))



