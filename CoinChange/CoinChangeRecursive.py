memo = {}

def count_coins(sum, index = 0):
    if (sum, index) in memo:
        return memo[(sum, index)]

    if sum == 0:
        return 1
    if sum < 0 or index >= len(coins):
        return 0

    memo[(sum,index)] = count_coins(sum - coins[index], index) + count_coins(sum, index + 1)
    return memo[(sum,index)]

