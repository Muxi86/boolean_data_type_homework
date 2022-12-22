from math import sqrt
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return sqrt(a) * sqrt(a) == a

a = int(input())

print(main(a))