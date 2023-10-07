
def running_sum1(nums):
    rs = []
    s = 0
    for n in nums:
        s = s + n
        rs.append(s)
    return rs

def running_sum(nums):
    i = 0
    return [ sum(nums[0:index+1])  for index, n in enumerate(nums) ]



nums = [1,2,3,4]
rs = running_sum(nums)
print(rs)
nums = [1,1,1,1,1]
rs = running_sum(nums)
print(rs)
nums = [3, 1, 2, 10, 1]
rs = running_sum(nums)
print(rs)