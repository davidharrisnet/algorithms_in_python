
s = []
s.append(1)
print(s)
s.append(2)
print(s)
s.append(3)
print(s)
s.append(4)
print(s)
print(f"pop {s.pop()}")

print(s)
print(f"pop {s.pop()}")
print(s)
print(f"pop {s.pop()}")
print(f"pop {s.pop()}")
print(s)
try:
    s.pop()
except IndexError as e:
    pass