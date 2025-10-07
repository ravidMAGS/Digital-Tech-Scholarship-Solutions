def count_coins(sum, index = 0):
    if sum == 0:
        return 1
    if sum < 0 or index >= len(coins):
        return 0

    return count_coins(sum - coins[index], index) + count_coins(sum, index + 1)
