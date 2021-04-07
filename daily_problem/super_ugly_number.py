"""A "super ugly number" is a positive number whose all prime factors
are in the given array.
Input:  primes[] = {2, 7, 13, 19}
        n = 11
Output: 28
Explanation: [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28]
                                                  ^ 11th number
Those are the first 11 numbers whose factors where in the  array.
"""


def find_super_ugly_number(arr, n: int):
    """return the nth super ugly number"""
    return 0


if __name__ == "__main__":
    find_super_ugly_number([2, 7, 13, 19], 11)

