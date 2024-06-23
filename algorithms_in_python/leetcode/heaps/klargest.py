from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    
    
klst = KthLargest(3, [4, 5, 8, 2])
print(klst.add(3))
print(klst.add(5))
print(klst.add(10))
print(klst.add(9))
print(klst.add(4))