def max_hamster(S: int, C: int, hamsters: list[list[int]] ):
    if S == 0:
        return 0
    low = 0
    high = C
    better_count = 0

    while low <= high:
        mid = (low + high) // 2
        
        if mid == 0:
            low = mid + 1
            continue
        cost = [h + g * (mid - 1) for h, g in hamsters]
        cost.sort()
        total_cost = sum(cost[:mid])

        if total_cost <= S:
            better_count = mid
            low = mid + 1
        else:
            high = mid -1
    return better_count