
def bubble(arr:list):
    for i in range(len(arr)):
        for j in range(len(arr) -1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

if __name__ == "__main__":
    l = list(range(10, 0, -1))
    print(l)
    bubble(l)
    print(l)

















