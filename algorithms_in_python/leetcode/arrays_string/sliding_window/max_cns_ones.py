from typing import List

''' 
  Given an array of 1's and 0's and an integer k. Determine
  the longets sub array of 1's given you may flip up to k 0's
  to 1. 
  For instance:
  s = [0,1,1,1,0,1,1,1,1,0]  is six from s[3] tp s[8]
  
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
    def longestOnes(self,nums: List[int], k: int) -> int:
        l = r = o = curr = max = 0
        
        while r < len(nums):
            if o < k:
                if nums[r] == 0:                    
                        o+=1
                r+=1                       
            else:
                curr = r - l
                if curr > max:
                    max = curr                    
                                                                        
                if nums[l] == 0:
                    o-=1
                l+=1
                    
        curr = r - l
            
        if curr > max:
            max = curr
            
        return max
        

if __name__ == "__main__":
    #nums = [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    #k = 2
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3

    s = Solution()
    print(s.longestOnes(nums,k))