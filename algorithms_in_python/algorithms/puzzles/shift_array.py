

def shift(a,d):
    l = a[d:]
    r = a[:d]
    return l + r




if __name__ == '__main__':
    arr = [1,2,3,4,5]
    s = shift(arr,2)
    print(s)