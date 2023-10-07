


def target_sum(arr, total):

    i = 0

    j = len(arr)-1


    if arr[0] > total:
        return false
    else:
        while arr[j] > total and i < j:
            j -= 1
    while(i < j):
        if arr[0] + arr[j] == total:
            return arr[0] + arr[l]







if __name__ == "__main__":
   arr = list(range(1,16))
   total = 13
   print(target_sum(arr, total))