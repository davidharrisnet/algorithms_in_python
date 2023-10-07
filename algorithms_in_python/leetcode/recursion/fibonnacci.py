

def fibonacci(i):
    if i <=1:
        return i
    else:
        return fibonacci(i -1) + fibonacci(i -2)

if __name__ == "__main__":
    f = fibonacci(6)


    print(f)