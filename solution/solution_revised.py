"""
Informal Structured Outline



Problem type:
   Pattern detecting


The gist of the problem:
    Find the least amount of operations within the restricted arithmatic rules
    divided by 2 , subtract 1, add 1
    Find the quickest way to let the number go down to 1

Input range:
    integer > 0, could up to 309 digits long


Concerned target:
    When encountering odd number, which even number to go to?

Goal:
    To decide correctly which even number to go to


What we have known:
    1. If the number is even, always go down to with divided by 2
    2. If the number is odd, there only 2 choices:
        either add + 1 or subtract 1
    3. Let's say n is odd number, then either n + 1 or n - 1
        is a number can be divided by 4
        E.g.
            Given a number line:
                4, 5, 6, 7, 8, 9, 10, 11, 12
            and their remainders of mod 4
                0, 1, 2, 3, 0, 1, 2,  3,  0
            If we only look at the odd number:
                5, 7, 9 ,11
            and their remainders of mod 4
                1, 3, 1, 3
            the number of their left and right is either 0 or 2
                For 5, it's 4 or 6(0, 2)
                For 7, it's 6 or 8(2, 0)
                For 9, it's 10 or 8(0, 2)
                For 11, it's 10 or 12(2, 0)

Conclusion:
    1. If it's an odd number, and then we choose the even number that can always be cut down by 4 at least
        In this way, we can make sure we choose the quickest way to 1
    2. The only exception is when the odd number is 3, because:
        3 -> 4 -> 2 -> 1
        3 -> 2 -> 1
    3. So the loop will stop if the number is less than or equal to 3

Must do in order to achieve the goal:
    1. For cases that the number is less than or equal to 3, we directly give the operations
        n = 3 -> 2
        n = 2 -> 1
    2. Otherwise, follow these 2 cases:
        even number -> always cut half 2
        odd number -> go to the number that can be cut half twice (divisible by 4)


===============================================================

Formal Description

-------------Definitions--------------

operations: Int
n: Int

---------------Steps-------------------

n := givenNumber,
operations := 0
{ n > 0 }

    DO n > 3:
        IF
            isEven(n) ->
                DO n % 2 = 0:
                    n := n / 2;
                    operations := operations + 1
                OD
            isOdd(n) ->
                IF
                    (n + 1) % 4 = 0 -> n := n + 1; operations + 1
                    (n - 1) % 4 = 0 -> n := n - 1; operations + 1
                FI
        FI
    OD;

    IF
        n = 3 -> operations := operations + 2
        n = 2 -> operations := operations + 1
        n = 1 -> skip;
    FI

{ n ≤ 3 }
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
        while n % 2 == 0:
            n //= 2
            operations += 1

    # Final step
    # Loop will end when 6 -> 3 or 4 -> 2
    # Add the corresponding operations
    if n == 3:
        operations += 2
    if n == 2:
        operations += 1

    return operations


# print(solution(1000000000))
for i in range(1, 1001):
    print(f"The number is {i}, the operations are {solution(i)}")
