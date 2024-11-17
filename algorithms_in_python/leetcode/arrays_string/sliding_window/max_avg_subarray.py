# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value.
# 75% speed
def find_max_avg(nums, k):
    # curr is the current sum of the window    
    ans = curr = sum(nums[:k])
    
    for j in range(len(nums) - k):
        curr += (nums[j + k] - nums[j])
        ans = max(curr,ans)
        
    return ans/k

# fastest
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:                    
    curr_window = []
    left = 0
    curr_sum = 0
    max_average = float('-inf')
    for right in range(len(nums)): 
        curr_sum += nums[right]
        curr_window.append(nums[right])        

        while left <= right and len(curr_window) >= k: 
            curr_window.pop()
            max_average = max(max_average, curr_sum / k)
            curr_sum -= nums[left]
            left += 1
    
    return max_average

if __name__ == "__main__":
    nums = [ 1, 12, -5, -6, 50, 3]
    #nums = [5]
    k = 4
    ans = findMaxAverage(nums, k)
    print(ans)