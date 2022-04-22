



def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key




if __name__ == "__main__":
    #a = [7, 4, 6, 1, 5, 2, 9, 3, 0, 8]
    a = [2,1]
    print(a)
    sort(a)
    print(a)