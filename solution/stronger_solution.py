"""
Insights:
    1. Always go with divide 2, repeating +1 or -1 won't get the shortest path
    2. When n is an odd number, if n + 1 can be cut twice, then n - 1 is never the smaller option;
            Otherwise, go with n - 1
    3. Simple while loop can do the work, no need for recursion

Approach:
Simply cut the number down along the way using while loop
When n is even number, count how many times it can be cut by 2 before become odd number
When n is odd number, use insight_2, and don't forget to add 1 operation because n + 1 or n - 1
Number cutting stops at 4, because for insight_2, number 3 is a special case
"""


def solution(n):
    return min_operations(int(n))


def min_operations(n):
    operations = 0
    while n > 3:
        # Odd number will go through this check
        # If n + 1 can be cut half at least twice
        # Then the operations of n - 1 are never going to be smaller than n + 1
        if n % 2 != 0:
            if (n + 1) % 4 == 0:
                operations += 1
                n += 1
            else:
                # Go with n - 1
                operations += 1
                n -= 1
        # Cut and count the even number operations
        times = times_divided_by_two(n)
        operations += times
        n //= (2 ** times)

    # Final step
    # Loop will end when 6 -> 3 or 4 -> 2
    # Add the corresponding operations
    if n == 3:
        operations += 2
    if n == 2:
        operations += 1

    return operations


def times_divided_by_two(n):
    times = 0
    while n % 2 == 0:
        n //= 2
        times += 1
    return times
