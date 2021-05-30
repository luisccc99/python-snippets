""""super ugly numbers" are positive numbers whose all prime factors
are in the given array.
Input:  primes[] = {2, 7, 13, 19}
        n = 11
Output: 28
Explanation: [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28]
                                                  ^ 11th number
Those are the first 11 numbers whose factors where in the array.
"""


def find_super_ugly_number(primes, n):
    """returns the nth super ugly number"""
    assert isSorted(primes), "given array wasn't sorted"
    k = len(primes)
    super_ugly_numbers = []

    # 1 is always the first ugly number
    super_ugly_numbers.append(1)

    # each element of this array is an iterator for the corresponding prime in primes
    multiple_of = [0]*k

    # this array behaves like next multiple variables of each prime in given primes
    next_multiple = primes[:]

    next_ugly_number = 0

    # loop until there are n elements in super ugly numbers:
    # find minimum number among the numbers in next_multiple
    # find multiple of minimum number in next_multiple
    # increment iterator by 1
    while (n > len(super_ugly_numbers)):
        print(multiple_of, next_multiple, super_ugly_numbers)
        next_ugly_number = min(next_multiple)
        super_ugly_numbers.append(next_ugly_number)
        for i in range(k):
            if (next_ugly_number == next_multiple[i]):
                multiple_of[i] += 1
                print(f"  m: {multiple_of[i]} ugly: {super_ugly_numbers[multiple_of[i]]}")
                next_multiple[i] = primes[i] * \
                    super_ugly_numbers[multiple_of[i]]
    return super_ugly_numbers[-1]


def isSorted(arr):
    for i in range(1, len(arr)):
        if (arr[i-1] > arr[i]):
            return False
    return True


if __name__ == "__main__":
    find_super_ugly_number([3, 5, 7, 11, 13], 30)
