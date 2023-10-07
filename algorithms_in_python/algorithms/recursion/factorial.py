



def factorial(n:int):
    if n == 0:
        print("1",end=" = ")
        return 1
    else:
        print(f"{n}",end=" * ")
        return n * factorial(n - 1)






if __name__ == "__main__":
  print(factorial(4))