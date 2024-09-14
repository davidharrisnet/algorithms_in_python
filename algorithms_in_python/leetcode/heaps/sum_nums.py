
from heapq import heapify, heappop, heappush, heapreplace


class Node():
    def __init__(self,val):
        self.val = val
    def __lt__(self,other):
        return self.val > other.val
    
def half_array():

    heap = [Node(5),Node(19) ,Node(8), Node(1)]

    target = sum([a.val for a in heap]) / 2
    
    heapify(heap)
    print([a.val for a in heap])
    ans = 0
    
    while target > 0:


        ans += 1
        t = heap[0].val
        heapreplace(heap, Node(heap[0].val / 2))
        target -= t /2
        print([a.val for a in heap])

   

    return ans

ans = half_array()
print(ans)


from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heappop(heap)
            target += x / 2
            heappush(heap, x / 2)
            print(heap)
        
        return ans

heap = [5, 19, 8, 1]
s = Solution()
ans = s.halveArray(heap)
print(ans)