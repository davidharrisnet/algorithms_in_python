import random

def getlist(size):
    return list(range(size,0,-1))

def random_int_list(low,high,length):
    return [random.randint(low,high) for _ in range(0,length)]

def print_arr(arr):
    " "
if __name__ == "__main__":
    print(random_int_list(0,10,6))