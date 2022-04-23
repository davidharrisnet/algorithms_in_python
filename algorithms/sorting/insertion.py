


"""
Algorithm 
To sort an array of size n in ascending order: 
1: Iterate from arr[1] to arr[n] over the array. 
2: Compare the current element (key) to its predecessor. 
3: If the key element is smaller than its predecessor, 
   compare it to the elements before. 
   Move the greater elements one position up to make space 
   for the swapped element.
"""


def insertion(theList):
    if len(theList) <= 1:
        return theList

    prev = 1

    for key in range(prev+1, len(theList)):
        if theList[key] < theList[prev]:
            temp = theList[key]
            theList[key] = theList[prev]
            theList[prev] = temp






if __name__ == "__main__":
    print("Hello")
    l = [ 1,4,6,2,6,7,0 ]
    insertion(l)
    print(l)