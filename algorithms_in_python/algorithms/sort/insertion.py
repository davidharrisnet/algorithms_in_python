
def insertion(arr):

    for k in range(1,len(arr)):
        key = arr[k]
        l = k -1
        while l >=0 and key < arr[l]:
            arr[l+1] = arr[l]
            l-=1
        arr[l+1] = key


if __name__ == "__main__":

    a = [6,8,2,1,5,3,7]
    print(a)
    insertion(a)
    print(a)

