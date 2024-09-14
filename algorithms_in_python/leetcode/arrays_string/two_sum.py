"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers 
that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return (left, right)
        if curr > target:
            right -= 1
        else:
            left += 1

    return False


nums = [1, 2, 4, 6, 8, 9, 14, 15]
nums.sort()
result = check_for_target(nums,13)
if(result):
    print(result[0],":", nums[result[0]])
    print(result[1],":",  nums[result[1]])