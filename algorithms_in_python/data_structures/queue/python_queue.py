import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

a = q.get()
print(a)
print(q.qsize())
q.get()
q.get()
print(q.qsize())