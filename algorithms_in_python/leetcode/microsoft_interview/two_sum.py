def twoSumNSquared(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0;
    j = 1;
    for i in range(0,len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """   
    
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    
        
   

arr = [3,1,2,5]
r = twoSum(arr,6)
print(r)