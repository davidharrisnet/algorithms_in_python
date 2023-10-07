# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value.

def find_max_avg(nums, k):
    # curr is the current sum of the window
    curr = 0
    for i in range(k):
        curr += nums[i] # first windows of average size k
    ans = curr
    for j in range(0, len(nums) -k):
        curr = curr + (nums[j + k] - nums[j])
        if curr > ans:
            ans = curr

    return ans/k


if __name__ == "__main__":
    nums = [ 1, 12, -5, -6, 50, 3]
    k = 4
    ans = find_max_avg(nums,k)
    print(ans)