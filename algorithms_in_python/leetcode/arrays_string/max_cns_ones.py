from typing import List

''' 
  Input:
  l    : left pointer
  r    : right pointer
  o    : number of 0's
  max  : the greatest value
  curr : the current value
  nums : the array of numbers

  while r < len(nums):
     if
'''

class Solution:
    def longestOnesSlow(self, nums: List[int], k: int) -> int:
        l = r = o = m = curr = 0
        while r < len(nums):
            while o <=k and r < len(nums):
                if nums[r] == 0:
                    o+=1
                if o <= k:
                    r+=1
                    curr+=1
            if curr > m:
                m = curr
            curr = o = 0
            l+=1
            r = l
        return m
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            r += 1
        return r - l


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    ##nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    #k = 3

    s = Solution()
    print(s.longestOnes(nums,k))