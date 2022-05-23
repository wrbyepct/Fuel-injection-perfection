from math import log
import sys

sys.setrecursionlimit(1500)

"""
Approaches:
Because the digits can be up to 309
The solution is only acceptable
when the time complexity is O(log n) or O(1)

Since O(1) seems to be unlikely
Let's try O(log n)
"""

"""
Details:
Because the dividing by 2 is more promising to get us the shortest path
    Maybe we can call recursive function to help the calculation
    since this is going to be logarithmic, the functions stack is close to log(n)
    this dramatically reduces the size if we are going to calculate the answer along the way
    
1. Let's pretend a function get_min_operations(n) will get us the answer

2. And we know when n = 1, the min operations will be 0,
       and when n = 2 will be 1
   So they are going to be our base cases
   
3. If n = 4(even), the operation will be 1 + get_min_operations(4 / 2)   

4. If n = 3(odd), the operations will be 1 + get_min_operations(3 - 1)    

5. But if we encounter an odd number like 15 or 9, 
       we really can't be sure which one of get_min_operations(n + 1) or get_min_operations(n - 1)
       will get us the shortest operations
       so we need to compare them
   Hence, when encounter odd number, 
   the answer will be 1 + min(get_min_operations(n - 1), get_min_operations(n + 1)) 
   for example 15, answer will be 1 + get_min_operations(15 + 1)
   for example 9, the answer will be 1 +1 get_min_operations(9 - 1)
   because they've compared the results
"""

min_op_dict = {}

called_times = {"times": 0}


def solution(n):
    return min_operations(int(n))


def min_operations(n):
    called_times["times"] += 1

    # Base cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    # To reduce the possible repeating recursion, store the calculated values in the dictionary
    # So if the key has already existed, simply return the stored value

    if n in min_op_dict:
        return min_op_dict[n]

    if is_power_of_two(n):
        min_op_dict[n] = round(log(n, 2))
        return min_op_dict[n]

    # If we don't have the key yet, create one and get answer from the actual calculation
    if n % 2 == 0:
        min_op_dict[n] = min_operations(n // 2) + 1
        return min_op_dict[n]

    if n + 1 in min_op_dict:
        n_plus_one = min_op_dict[n + 1]

    else:
        min_op_dict[n + 1] = min_operations((n + 1) // 2) + 1
        n_plus_one = min_op_dict[n + 1]

    if n - 1 in min_op_dict:
        n_minus_one = min_op_dict[n - 1]

    else:
        min_op_dict[n - 1] = min_operations((n - 1) // 2) + 1
        n_minus_one = min_op_dict[n - 1]

    min_op_dict[n] = min(n_plus_one, n_minus_one) + 1
    # Print when n + 1 is smaller
    if n_plus_one >= n_minus_one:
        print(f"The number is: {n}, the operations are: {min_op_dict[n]}\n"
              f"The previous number is {n - 1}, the operations are: {min_op_dict[n - 1]}\n"
              f"The following number is {n + 1}, the operations are: {min_op_dict[n + 1]}\n")

    return min_op_dict[n]


def is_power_of_two(number):
    power = log(number, 2)
    return number == 2 ** round(power)


for i in range(2, 1001):
    solution(i)

# print(min_operations(10**309))
# print(called_times["times"])

# print(solution("4"))
# print(solution("15"))
# print(solution("100"))