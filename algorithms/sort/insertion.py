



def sort(arr):
    global swap_count
    for k in range(1, len(arr)): # start with the second item in the list
        key = arr[k]  # this is the key

        l = k-1
        while l >= 0 and key < arr[l]:  # Then look at all the tokens to the left of key
            # The key is < arr[i] on the left,
            arr[l+1] = arr[l]  # Move arr[l] to the right
            swap_count += 1
            l -= 1
        arr[l + 1] = key  #the item not < key receives key ( arr[l+1] has already been moved,
                                                             # so we can overwrite it. )

if __name__ == "__main__":
    a = [7, 4, 6, 1, 5, 2, 9, 3, 0, 8]
    swap_count = 0
    print(a)
    sort(a)
    print(a)