memo = {}

def coin_change(remaining, index=0):
    if (remaining, index) in memo:
        return memo[(remaining, index)]

    if remaining == 0:
        return 1
    if remaining < 0:
        return 0

    total_ways = 0
    for i in range(index, len(coins)):
        total_ways += coin_change(remaining - coins[i], i)

    memo[(remaining, index)] = total_ways
    return total_ways
