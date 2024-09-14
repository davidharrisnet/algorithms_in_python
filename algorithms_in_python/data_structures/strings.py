

a = "12"
# you can access a string with an array index
print(a[1])

# But they are immutable, so you can't change them
# a[3] = "a"
# you can append a string, but this actually creates a new one
a += "."
print(a)

# Turn a string into an array
arr = list(a)
print(arr)
# this is how you turn an array into a string
a2 = "".join(arr)
print(type(a2))


arr = list(a)
i = 0
j = len(a) -1
while i < j:
    arr[i] , arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

arr2 = "".join(arr)
print(arr2)

arr = "I am a big apple."
# reverse words
tokens = arr.split(" ")
i = 0
j = len(tokens) -1
while i < j:
    tokens[i] , tokens[j] = tokens[j], tokens[i]
    i += 1
    j -= 1

print(tokens)