import random

def getlist(size=20):
    return list(range(size,0,-1))

def random_list(low=0,high=20,length=20):
    return [random.randint(low,high) for _ in range(0,length)]

def print_arr(arr):
    " "
if __name__ == "__main__":
    print(random_list(0,10,100))
    
    
