from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    target = 4
    result = s.twoSum(nums, target)
    print(result)