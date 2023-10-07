import random

def random_int_list(low,high,length):
    return [random.randint(low,high) for _ in range(0,length)]





if __name__ == "__main__":
    print(random_int_list(0,10,6))