def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    if a>0 and b>0 and a!=0:
     return ("False")
    if a<0 and b<0 and a!=0:
      return ("True")
    if a>0 and b<0 and a!=0:
      return ("False")
    if a<0 and b>0  and a!=0:
      return ("False")
print(main(-5,-5))




