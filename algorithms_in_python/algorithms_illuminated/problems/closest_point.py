import random
import copy
import math
def sortX(arr:list):
        
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        sortX(L)
        sortX(R)
        
        i = l = r = 0
        while l < len(L) and r < len(R):
            if L[l].x < R[r].x:
                arr[i] = L[l]
                l += 1
            else:
                arr[i] = R[r]
                r += 1
            i += 1
        while l < len(L):
            arr[i] = L[l]
            i += 1
            l += 1
        while r < len(R):
            arr[i] = R[r]
            r += 1
            i += 1
     
def sortY(arr:list):
        
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        sortY(L)
        sortY(R)
        
        i = l = r = 0
        while l < len(L) and r < len(R):
            if L[l].y < R[r].y:
                arr[i] = L[l]
                l += 1
            else:
                arr[i] = R[r]
                r += 1
            i += 1
        while l < len(L):
            arr[i] = L[l]
            i += 1
            l += 1
        while r < len(R):
            arr[i] = R[r]
            r += 1
            i += 1
 

class Point():
    def __init__(self, x, y):
        self.x = y
        self.y = x
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
def random_point() -> Point:
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    return Point(x,y)


def generate_points(count) -> list:
    points = []
    for _ in range(0,count):
        points.append(random_point())
    return points

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2) 

def closest_pair(arr,start,end):
    if start == end:
        return -1
    else 

def main():
    points = generate_points(10)
    
    #pointsX = copy.deepcopy(points)
    pointsX = points.copy()   
    #pointsY = copy.deepcopy(points)
    pointsY  = points.copy()  
    sortX(pointsX)    
    sortY(pointsY)
    
    
    
    

if __name__ == "__main__":
    main()