def counting_sort(arr: list[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: list[int]):
    if not arr:
        return
        
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def max_hamster(S: int, C: int, hamsters: list[list[int]]):
    if S == 0:
        return 0, 0
        
    low = 0
    high = C
    max_count = 0
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        cost = [h + g * (mid - 1) for h, g in hamsters]
        
        radix_sort(cost)
        
        total_food = sum(cost[:mid])

        if total_food <= S:
            max_count = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return max_count, iterations