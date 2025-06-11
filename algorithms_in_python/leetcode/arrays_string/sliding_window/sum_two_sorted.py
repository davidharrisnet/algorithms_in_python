"""
  https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/

  Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a 
  pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. 
  (In Two Sum, the input is not sorted).

  For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

  Note: a similar version of this problem can be found on LeetCode: 167. Two Sum II - Input Array Is Sorted
"""


def sumtwo(nums,target):
    l = 0
    r = len(nums) -1
    while nums[r] > target:
        r -= 1
        
    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            return True, nums[l], nums[r]       
        elif sum < target:
            l+=1
        else: # sum > target
            r-=1
    return False

#nums = [ 1, 2, 4, 6, 8, 9, 14, 15]
#target = 22
nums = [ 3,4,6,9]
target = 10
print(sumtwo(nums,target))