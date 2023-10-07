


def sort(arr):
    for k in range(1,len(arr)):
        key = arr[k]
        l = k-1

        while l >=0 and key < arr[l]:
            arr[l+1] = arr[l]
            l-=1
        arr[l+1] = key



if __name__ == "__main__":
    arr = [ 8,9,4,6,7,8,5,4,3,2,1,0]
    print(arr)
    sort(arr)
    print(arr)