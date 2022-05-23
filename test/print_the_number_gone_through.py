from math import log

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
   
6. However, if you observed the results of odd numbers
        you would notice the subtle difference between n + 1 and n - 1
        if n + 1 % 4 == 0(the even number can be cut half at elast twice)
        then the result of n - 1 is never gonna be smaller than n + 1
           
"""

min_op_dict = {}

called_times = {"times": 0}


def solution(n):
    return min_operations(int(n))


def min_operations(n):
    called_times["times"] += 1
    # Print every checking number
    # print(f"Checking number: {n}")
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

    if n % 2 == 0:
        return fasten_even_num_dict_store(n)

    # Check if n + 1 is not divisible by 4
    if (n + 1) % 4 != 0:
        # If this happened, choose n_minus_one
        # Because the chance for n_plus_one is smaller than n_minus_one is zero

        min_op_dict[n] = fasten_even_num_dict_store(n - 1) + 1
        return min_op_dict[n]
    # Otherwise, choose n_plus_one

    min_op_dict[n] = fasten_even_num_dict_store(n + 1) + 1

    return min_op_dict[n]


def fasten_even_num_dict_store(n):
    power_of_two = 1024
    for i in range(10, 0, -1):
        if n % power_of_two == 0:
            min_op_dict[n // power_of_two] = min_operations(n // power_of_two)
            min_op_dict[n] = min_op_dict[n // power_of_two] + i
            return min_op_dict[n]
        power_of_two //= 2


# def is_power_of_two(number):
#     power = log(number, 2)
#     return number == 2 ** round(power)


# for j in range(1, 1001):
#     print(f"This number is {j}, the operations are: {solution(j)}")


print(f"The minimum operations are: {min_operations(10**309 - 1)}")
print(f"Recursion times: {called_times['times']}")
