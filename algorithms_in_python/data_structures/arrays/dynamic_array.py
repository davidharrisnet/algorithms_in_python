class Array(object):

    def __init__(self, initial_size):  # Constructor
        self.__array = [None] * initial_size  # The array stored as a list
        self.nItems = 0  # No items in array initially

    def insert(self, item):  # Insert item at end
        self.__array[self.nItems] = item  # Item goes at current end
        self.nItems += 1  # Increment number of items

    def search(self, item):
        for j in range(self.nItems):  # Search among current
            if self.__array[j] == item:  # If found,
                return self.__array[j]  # then return item

        return None

    def delete(self, item):  # Delete first occurrence
        for j in range(self.nItems):  # of an item
            if self.__array[j] == item:  # Found item
                for k in range(j, self.nItems):  # Move items from
                    self.__array[k] = self.__array[k + 1]  # right over 1
                self.nItems -= 1  # One fewer in array now
                return True  # Return success flag

        return False  # Made it here, so couldn't find the item


    def traverse(self, function=print):  # Traverse all items
        for j in range(self.nItems):  # and apply a function
            function(self.__array[j])
    def __str__(self):
        result = "["
        for j in range(self.nItems-1):  # and apply a function
            result += f"{self.__array[j]},"
        result+=f"{self.__array[self.nItems-1]}]"
        return result

if __name__ == "__main__":
    a = Array(2);

    a.insert(2)
    a.insert(3)
    a.insert(4)
    print(a)