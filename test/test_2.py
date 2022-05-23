def solution(n):
    return min_operations(int(n))


def min_operations(n):
    # Base cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    # To reduce the possible repeating recursion, store the calculated values in the dictionary
    # So if the key has already existed, simply return the stored value
    # if n in min_op_dict:
    #     print(f"Accessed dict key of {n}")
    #     return min_op_dict[n]

    if n % 2 == 0:
        return min_operations(n // 2) + 1
    return min(min_operations(n + 1), min_operations(n - 1)) + 1
