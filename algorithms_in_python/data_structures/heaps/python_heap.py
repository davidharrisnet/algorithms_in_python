import heapq

h = []

arr = [4,6,5,7,8,9,0,1,2]

for a in arr:
    heapq.heappush(h,a)
print(h)
heapq.heapify(arr)
print(arr)
for _ in range(len(arr)):
    print(heapq.heappop(arr))
    
    
from queue import PriorityQueue

q = PriorityQueue()

q.put(1,"A")
q.put(2, "B")
q.put(3, "C")
q.put(4, "D")
q.put(5, "E")
q.put(6, "F")

q.qsize()