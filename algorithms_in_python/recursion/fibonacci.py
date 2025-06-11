# 0 1 1 2 3 590 8 ...
# 0 = 1, 1 = 1, n = (n-1) + (n-2)

def fib_linear(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 1,1
        for i in range(1,n):
            a, b = b, a + b
        
        return a

def fib_recurse(n):
    assert(n >= 0)
    if n <= 1:
        return n
  
    return fib_recurse(n -1) + fib_recurse(n -2)
    
if __name__  == "__main__":
    
   
    for i in range(1,10):
        print(fib_linear(i))
        print(fib_recurse(i))
        print()
    
    
    