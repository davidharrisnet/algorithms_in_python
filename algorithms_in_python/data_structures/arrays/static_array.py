from array import array


class IndexOutOfRange(Exception):
    def __init__(self, value):
        super().__init__("Index out of range")
        self.value = value



class StaticArray:
    def __init__(self):
        self.static_array = [1, 2, 3]
        self.len = 3
        self.capacity = 3

    def __str__(self):
        return str([i for i in self.static_array])

    def size(self):
        return self.len

    def __getitem__(self, index):
        if index < self.len - 1:
            return self.static_array[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index < self.len - 1:
            self.static_array[index] = value
        else:
            raise IndexError("Index out of range")

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    raise IndexOutOfRange(2)

    size = 10
    sii = StaticArray()

    print(sii[1])
    sii[0] = -5
    print(sii)
