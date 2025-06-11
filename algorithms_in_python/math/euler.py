#var('x y')
import math
import numpy as np

def f(x,y):
    return x + 4 * math.sqrt(y)

def main(x0, y0, h, end):
    #x0 = 0
    #y0 = 5
    #h = 0.1
    #end = 2
    x_values = np.arange(x0, end + h, h)
   
    y_values = [y0]
    y_n = y0
    for x_n in x_values:
        y_n = y_n + h*f(x_n, y_n)
        y_n = y_n * 2 - (3 * x_n)
        y_values.append(y_n)
    
    approximation = list(zip(x_values, y_values))
    print(approximation[len(approximation)-1])
    
if __name__ == "__main__":
    
    main(0,5,0.1,2)