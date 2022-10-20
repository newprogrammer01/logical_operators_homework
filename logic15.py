def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a//100
    x2=a%100//10
    x3=a%10
    x4=x1+x2+x3
    return (a>=100 and a<1000 and (x4)%2==1)
print(main(264))
