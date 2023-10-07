
def hourglass_sum(arr):

    sums = []
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if i + 2 <= len(arr) - 1 and j + 2 <= len(arr) - 1:
                sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                      arr[i + 1][j + 1] + \
                      arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                sums.append(sum)
    return max(sums)


if __name__ == '__main__':
    arr=[[1,1,1,1,2,3], [1,1,1,1,2,3], [1,1,1,1,2,3], [1,1,1,1,2,3],
         [1,1,1,1,2,3], [1,1,1,1,2,3]]
    m = hourglass_sum(arr)
    print(m)