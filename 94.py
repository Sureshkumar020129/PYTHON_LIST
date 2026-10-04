print(" Find the longest increasing subsequence in a list. ")
numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80]
def longest_increasing_subsequence(nums):
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    index = dp.index(max_length)

    lis = []
    while index != -1:
        lis.append(nums[index])
        index = prev[index]

    return lis[::-1]
    